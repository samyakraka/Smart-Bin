#include <Arduino.h>

// Ultrasonic sensor pins
const int trigPin = 9; //Mark this trigPin
const int echoPin = 10; //Mark this echoPin

// Maximum distance the sensor can measure (in cm)
const int maxDistance = 50;

long duration;
int distance;

void setup() {
  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);
  
  // Initialize sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  Serial.println("Smart Dustbin Offline Version Initialized");
}

void loop() {
  // Measure distance using ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  
  distance = duration * 0.034 / 2; // Convert to cm
  
  // Calculate garbage level percentage
  int percentage = map(distance, 0, maxDistance, 100, 0);
  percentage = constrain(percentage, 0, 100); // Ensure percentage is between 0 and 100
  
  // Send data via serial
  Serial.print("Garbage Level: ");
  Serial.print(percentage);
  Serial.println("%");
  
  delay(10000); // Wait for 60 seconds before next reading
}

