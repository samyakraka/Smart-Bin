from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Path to the JSON data file
DATA_FILE = os.path.join('data', 'garbage_data.json')

@app.route('/')
def index():
    # Read the latest 20 records
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        latest_data = data[-20:][::-1]  # Get last 20 entries and reverse for latest first
    except Exception as e:
        latest_data = []
        print(f"Error reading JSON file: {e}")
    return render_template('index.html', statuses=latest_data)

@app.route('/garbage-status', methods=['GET'])
def garbage_status():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        latest_data = data[-20:][::-1]  # Get last 20 entries and reverse for latest first
        return jsonify({'status': 'success', 'data': latest_data}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
