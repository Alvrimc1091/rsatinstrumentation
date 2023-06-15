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

# LM35DZ PIN CONNECTION
Make sure you have the necessary permissions to access the analog input on your Raspberry Pi. By default, 
the gpio group has the required permissions. You can add your user to the gpio group by running the following command:

sudo usermod -aG gpio <your_username>

After adding your user to the gpio group, you will need to reboot your Raspberry Pi for the changes to take effect.

To connect the LM35DZ sensor to your Raspberry Pi:

  - Connect the LM35DZ's VCC (Positive) pin to the 3.3V pin on the Raspberry Pi.
  - Connect the LM35DZ's GND (Ground) pin to a ground pin on the Raspberry Pi.
  - Connect the LM35DZ's Vout pin to an analog input pin (e.g., GPIO 0 / BCM pin 17) on the Raspberry Pi.
  - 
Once you have made the connections and saved the script as a .py file, you can run it to read temperature data from the LM35DZ sensor on your Raspberry Pi.


# DS18B20 PIN CONNECTION

To use the DS18B20 temperature sensor with your Raspberry Pi, follow these steps:

  - Connect the DS18B20 sensor to the GPIO pin 4 (BCM pin 4) on your Raspberry Pi.
  - Optionally, add a 4.7kΩ pull-up resistor between the DS18B20's data line and the 3.3V pin on the Raspberry Pi.
  - Enable the 1-Wire interface on your Raspberry Pi by following these steps:
    - Open the terminal on your Raspberry Pi.
    - Run the command sudo raspi-config.
    - Select "Interfacing Options" and press Enter.
    - Select "1-Wire" and press Enter.
    - Choose "Yes" to enable the 1-Wire interface.
    - Reboot your Raspberry Pi for the changes to take effect.
  - Make sure the DS18B20 sensor is properly connected.
  - Save the Python script as a .py file and run it to read temperature data from the DS18B20 sensor on your Raspberry Pi.

The script will continuously read the temperature from the DS18B20 sensor and display it in Celsius.
