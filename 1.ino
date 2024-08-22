#include <Arduino_LSM6DS3.h>  // Include the LSM6DS3 library for the gyroscope

// Variables to store the gyroscope data
float x, y, z;

void setup() {
  // Initialize the serial communication at 9600 baud
  Serial.begin(9600);
  
  // Wait for serial port to connect. Needed for native USB port only
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // Initialize the LSM6DS3 gyroscope
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
  
  // Print IMU initialization success message
  Serial.println("IMU initialized successfully!");
}

void loop() {
  // Check if gyroscope data is available
  if (IMU.gyroscopeAvailable()) {
    // Read gyroscope data for x, y, z axes
    IMU.readGyroscope(x, y, z);

    // Print the gyroscope data to the serial monitor
    Serial.print("Gyroscope X: ");
    Serial.print(x);
    Serial.print(" dps, Y: ");
    Serial.print(y);
    Serial.print(" dps, Z: ");
    Serial.print(z);
    Serial.println(" dps");
  }

  // Add a delay to reduce the output rate
  delay(1000); // Delay of 1 second between readings
}
