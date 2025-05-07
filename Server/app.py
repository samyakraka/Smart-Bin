from flask import Flask, render_template, jsonify
import json
import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

# Load environment variables from .env file
load_dotenv()

# Configure application
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key-for-dev')
app.config['JSON_SORT_KEYS'] = False
app.config['ENV'] = os.environ.get('FLASK_ENV', 'production')
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'

# Set up logging
if not os.path.exists('logs'):
    os.makedirs('logs')
file_handler = RotatingFileHandler('logs/smart_bin.log', maxBytes=10240, backupCount=10)
file_handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
))
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Smart Bin server startup')

# Path to the JSON data file
data_directory = os.environ.get('DATA_DIRECTORY', 'data')
if not os.path.exists(data_directory):
    os.makedirs(data_directory)
DATA_FILE = os.path.join(data_directory, 'garbage_data.json')

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

@app.route('/')
def index():
    # Read the latest 20 records
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        latest_data = data[-20:][::-1]  # Get last 20 entries and reverse for latest first
    except Exception as e:
        latest_data = []
        app.logger.error(f"Error reading JSON file: {e}")
    return render_template('index.html', statuses=latest_data)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/garbage-status', methods=['GET'])
def garbage_status():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            
        # Return all data for filtering on the client side
        # Sort by timestamp to ensure newest data is first
        sorted_data = sorted(data, key=lambda x: x['timestamp'], reverse=True)
        
        return jsonify({'status': 'success', 'data': sorted_data}), 200
    except Exception as e:
        app.logger.error(f"Error reading JSON file: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Only run the development server if script is executed directly
# This won't run on Vercel's serverless environment
if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    # In production, you might want to use 0.0.0.0 to listen on all interfaces
    host = os.environ.get('HOST', '127.0.0.1')  # Changed from 0.0.0.0 to 127.0.0.1 for local development
    app.logger.info(f"Starting application on {host}:{port}")
    app.run(host=host, port=port)
