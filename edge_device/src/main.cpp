#include <Arduino.h>

// Sensor Pin Definitions
const int PIN_SOUND = 33;        // Analog output (AO) from LM393/KY-038
const int PIN_IR_OBSTACLE = 25;  // Digital output (DO) from IR sensor

void setup() {
  Serial.begin(115200);
  
  pinMode(PIN_SOUND, INPUT);
  pinMode(PIN_IR_OBSTACLE, INPUT);
  
  Serial.println("--- Dual Sensor Calibration Test Started ---");
  Serial.println("Waiting for readings...");
  delay(1000);
}

void loop() {
  // 1. Read the sensors
  int irValue = digitalRead(PIN_IR_OBSTACLE);
  int soundValue = analogRead(PIN_SOUND);
  
  // 2. Format the IR output for readability
  // Note: Most IR sensors pull LOW (0) when an object is detected
  String irStatus = (irValue == LOW) ? "OBSTACLE (0)" : "CLEAR    (1)";
  
  // 3. Print the results side-by-side
  Serial.print("IR: ");
  Serial.print(irStatus);
  Serial.print("   |   Sound (Raw Analog): ");
  Serial.println(soundValue);
  
  // 4. Short delay: 50ms is fast enough to catch sound spikes, 
  // but slow enough to read the text on the screen.
  delay(50); 
}