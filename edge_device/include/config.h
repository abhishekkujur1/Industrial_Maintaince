#ifndef CONFIG_H
#define CONFIG_H

// --- Wi-Fi Credentials ---
const char* WIFI_SSID = "YOUR_WIFI_NAME";
const char* WIFI_PASSWORD = "YOUR_WIFI_PASSWORD";

// --- MQTT Settings ---
const char* MQTT_BROKER = "192.168.1.X"; // Replace with your laptop/server IP
const int MQTT_PORT = 1883;
const char* MQTT_TOPIC = "machine/sensor_data";
const char* MQTT_CLIENT_ID = "ESP32_Predictive_Node_1";

// --- Sensor Pin Definitions ---
// Analog Pins (ADC)
const int PIN_SOUND = 33;

// Digital Pins
const int PIN_IR_OBSTACLE = 25;

// --- Sampling Settings ---
// How often to send data to the server (in milliseconds)
const unsigned long PUBLISH_INTERVAL = 1000; // 1 second

#endif