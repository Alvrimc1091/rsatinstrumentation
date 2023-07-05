# ------ PINS ------
# VCC/VIN -> 3.3V (PIN 1)
# GND -> GND (PIN 6)
# SCL -> SCL (PIN 5)
# SDA -> SDA (PIN 3)

import bmpsensor
import time
while True:
    temp, pressure, altitude = bmpsensor.readBmp180()
    print("Temperature is ",temp)  # degC
    print("Pressure is ",pressure) # Pressure in Pa 
    print("Altitude is ",altitude) # Altitude in meters
    print("\n")
    time.sleep(2)
