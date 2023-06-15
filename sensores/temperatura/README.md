# AHT10 PIN CONNECTION
Make sure you have the smbus2 library installed by running pip install smbus2 in your terminal.

To connect the AHT10 sensor to your Raspberry Pi:

  - SDA (Serial Data Line): Connect to the GPIO 2 pin (BCM pin 2) on the Raspberry Pi.
  - SCL (Serial Clock Line): Connect to the GPIO 3 pin (BCM pin 3) on the Raspberry Pi.
  - VCC (Power): Connect to a 3.3V pin (e.g., pin 1) on the Raspberry Pi.
  - GND (Ground): Connect to a ground pin (e.g., pin 9 or 14) on the Raspberry Pi.

Ensure that you have enabled the I2C interface on your Raspberry Pi as mentioned in the previous response. 
After making the connections and enabling I2C, you can run the Python script to read temperature and humidity 
data from the AHT10 sensor on your Raspberry Pi.
