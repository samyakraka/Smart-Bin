
---

# **Smart-Bin Project**

### **Project Overview**

The **Smart-Bin System** is an IoT-based project designed to monitor garbage levels in dustbins placed in various public areas (e.g., temples). The system uses an **Ultrasonic Sensor (HC-SR04)** to detect the level of garbage and sends the data to an **Arduino Uno**, which then transmits the information via serial communication to a connected computer. This data is processed using a **Python** script and is displayed in real-time through a **Flask** web interface.

---

## **Features**

- Real-time monitoring of garbage levels in dustbins.
- Displays garbage level percentage on a web interface.
- Stores historical garbage data and displays the latest 20 entries.
- Automatic update of garbage levels every minute.
- Simple and user-friendly web interface.

---

## **System Components**

### **Hardware:**
- **Arduino Uno** (microcontroller)
- **HC-SR04 Ultrasonic Sensor** (for distance measurement)
- **USB Cable** (to connect Arduino to the computer)
- **Connecting Wires** (to wire components together)

### **Software:**
- **Arduino IDE** (to upload code to Arduino)
- **Python 3** (for reading serial data)
- **Flask** (to build the web interface)
- **HTML/CSS/JavaScript** (for front-end web development)
- **JSON** (for managing live data / for managing database)

---

## **Project Structure**

```bash
Smart-Bin/
├── Arduino_Code/
│   └── smart_bin.ino             # Arduino code for measuring garbage levels
├── Server/
│   ├── app.py                    # Flask app to serve web interface and data
│   ├── read_serial.py             # Python script to read Arduino serial data
│   ├── requirements.txt           # Python dependencies
│   ├── data/
│   │   └── garbage_data.json      # JSON file to store garbage level data
│   ├── templates/
│   │   └── index.html             # Web page template for displaying data
│   └── static/
│       └── style.css              # Styling for the web page
└── README.md                      # Project documentation
```

---

## **How It Works**

1. **Sensor Input:** 
   The ultrasonic sensor measures the distance to the garbage level in the bin.
   
2. **Arduino Processing:** 
   The Arduino reads the sensor data and calculates the percentage of garbage in the bin (based on distance).
   
3. **Serial Communication:**
   The Arduino sends the calculated garbage level percentage to the computer via serial communication.

4. **Python Script:**
   A Python script (`read_serial.py`) reads the serial data and stores it in a JSON file (`garbage_data.json`).

5. **Flask Web Server:**
   The Flask application serves the data on a web interface, allowing users to view real-time garbage levels.

---

## **Hardware Setup**

1. **HC-SR04 Ultrasonic Sensor Pinout:**
   - **VCC:** 5V (Arduino)
   - **GND:** GND (Arduino)
   - **Trig:** Digital Pin 9 (Arduino)
   - **Echo:** Digital Pin 10 (Arduino)

2. **Connections:**

| HC-SR04 Pin | Arduino Pin       |
|-------------|-------------------|
| VCC         | 5V                |
| GND         | GND               |
| Trig        | Digital Pin 9      |
| Echo        | Digital Pin 10     |

3. **Power Supply:**
   - Ensure Arduino is powered using the USB cable connected to your computer.

---

## **Software Setup**

### **1. Arduino Code Upload**

1. Open `Arduino_Code/smart_dustbin.ino` in the Arduino IDE.
2. Select your correct **Board** and **Port** from the Arduino IDE.
3. Upload the code to your Arduino.

### **2. Python Environment Setup**

1. Navigate to the **Server** directory:
   ```bash
   cd Smart-Bin/Server
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Flask Web Server Setup**

1. Navigate to the **Server** directory:
   ```bash
   cd Smart-Bin/Server
   ```

2. Run the Python script to read serial data from Arduino:
   ```bash
   python read_serial.py
   ```

3. In another terminal, start the Flask web server:
   ```bash
   python app.py
   ```

4. Open a web browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Usage**

- Once the system is set up, the Arduino will continuously measure the garbage level and send it to the Python script.
- The Flask server will display this data on the web interface, refreshing automatically every minute.

---

## **Sample Web Interface**

The web interface displays a table with the latest garbage level readings (in percentage), showing the timestamp for each entry.

---

## **Contributing**

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. Here are a few ideas for improvements:
- Adding more sensors to monitor multiple bins.
- Implementing real-time notifications (e.g., when a bin is full).
- Creating a mobile app interface for easier monitoring.

---

## **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## **Troubleshooting**

1. **Arduino Not Detected:**
   - Ensure you have selected the correct **Board** and **Port** in the Arduino IDE.
   - Check the USB connection.

2. **Serial Data Not Displayed:**
   - Ensure the `read_serial.py` script is running.
   - Check the COM port in the Python script and adjust accordingly.

3. **Web Interface Not Loading:**
   - Verify the Flask server is running (`app.py`).
   - Ensure your browser is pointing to the correct URL (`http://127.0.0.1:5000/`).

---

## **Future Enhancements**

- **Remote Monitoring:** Connect the system to a cloud platform to allow remote monitoring from anywhere.
- **Full Bin Alerts:** Send notifications (via SMS/Email) when the garbage bin is about to overflow.
- **Data Analytics:** Analyze the data collected over time to predict when bins will need to be emptied.

---

