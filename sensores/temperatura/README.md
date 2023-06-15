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
