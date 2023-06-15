import time
import os

# LM35DZ analog pin
LM35_PIN = 0

# Read temperature from LM35DZ sensor
def read_temperature():
    # Read the raw value from the analog pin
    raw_value = read_analog_value(LM35_PIN)
    
    # Calculate the temperature in Celsius
    temperature = (raw_value / 1023.0) * 3.3
    temperature = temperature * 100.0
    
    return temperature

# Read analog value from specified pin
def read_analog_value(pin):
    # Open the file that provides access to the analog pin value
    with open("/sys/bus/iio/devices/iio:device0/in_voltage{}/raw".format(pin), "r") as f:
        value = int(f.read().strip())
    return value

# Main loop
while True:
    temperature = read_temperature()
    print("Temperature: {:.2f}°C".format(temperature))
    time.sleep(1)
