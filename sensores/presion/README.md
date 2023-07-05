To connect the BMP180 sensor to your Raspberry Pi 4, you will need to establish an I2C connection. The Raspberry Pi 4 has built-in I2C pins, which are as follows:

- SDA (Serial Data Line): Connect to the GPIO 2 pin (BCM pin 2) on the Raspberry Pi.
- SCL (Serial Clock Line): Connect to the GPIO 3 pin (BCM pin 3) on the Raspberry Pi.
- VCC (Power): Connect to a 3.3V pin (e.g., pin 1) on the Raspberry Pi.
- GND (Ground): Connect to a ground pin (e.g., pin 9 or 14) on the Raspberry Pi.

Make sure to double-check your specific Raspberry Pi model and pinout diagram to ensure the correct pin connections.

Additionally, ensure that the `i2c-dev` kernel module is enabled on your Raspberry Pi. You can enable it by following these steps:

1. Open the terminal on your Raspberry Pi.
2. Run the command `sudo raspi-config`.
3. Select "Interfacing Options" and press Enter.
4. Select "I2C" and press Enter.
5. Choose "Yes" to enable the I2C interface.
6. Reboot your Raspberry Pi for the changes to take effect.

Once you have made the connections and enabled the I2C interface, you should be able to run the Python script to communicate with the BMP180 sensor on your Raspberry Pi 4.


In orden to get data and transfer it to the csv, run the command:
    python3 bmp180.py
