import serial
import json
import time
import os
from datetime import datetime

# Configuration
SERIAL_PORT = 'COM8'  #Replace with your Arduino's COM port
BAUD_RATE = 9600
DATA_FILE = 'data/garbage_data.json'

def initialize_json(file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    if not os.path.isfile(file_path):
        with open(file_path, 'w') as f:
            json.dump([], f)  # Initialize the file with an empty list

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("JSON file is empty or corrupted. Reinitializing...")
        data = []
    return data

def read_serial(ser):
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Received line: {line}")
            else:
                print("Received empty line or no data.")

            # Only process if the line has "Garbage Level:" prefix
            if line.startswith("Garbage Level:"):
                percentage = int(line.split(":")[1].replace("%", "").strip())
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data_entry = {"timestamp": timestamp, "level": percentage}
                
                # Append to JSON file
                data = read_json(DATA_FILE)
                data.append(data_entry)
                
                # Optionally, limit to the latest 100 entries
                if len(data) > 100:
                    data = data[-100:]
                
                # Write updated data back to the file
                with open(DATA_FILE, 'w') as f:
                    json.dump(data, f, indent=4)
                
                print(f"Logged Data: {data_entry}")
            else:
                print(f"Unexpected data format: {line}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(1)

if __name__ == "__main__":
    initialize_json(DATA_FILE)
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        print(f"Connected to {SERIAL_PORT} at {BAUD_RATE} baud.")
        read_serial(ser)
    except serial.SerialException as e:
        print(f"Could not open serial port {SERIAL_PORT}: {e}")
