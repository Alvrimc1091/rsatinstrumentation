import time

# Path to the DS18B20 sensor
SENSOR_PATH = "/sys/bus/w1/devices/28-*/w1_slave"

# Read temperature from DS18B20 sensor
def read_temperature():
    # Get the list of available sensors
    sensor_list = get_sensor_list()
    
    # Read the temperature from the first sensor
    if sensor_list:
        sensor_path = sensor_list[0]
        temperature = read_sensor(sensor_path)
        return temperature
    
    return None

# Get the list of available DS18B20 sensors
def get_sensor_list():
    try:
        # Read the device folder to get the list of sensors
        sensor_folders = [folder for folder in os.listdir("/sys/bus/w1/devices/") if folder.startswith("28-")]
        sensor_list = [os.path.join("/sys/bus/w1/devices/", folder, "w1_slave") for folder in sensor_folders]
        return sensor_list
    except Exception as e:
        print("Error: Failed to get the list of DS18B20 sensors -", str(e))
        return []

# Read temperature from a specific DS18B20 sensor
def read_sensor(sensor_path):
    try:
        with open(sensor_path, "r") as f:
            lines = f.readlines()
        
        if lines[0].strip().endswith("YES"):
            temperature_line = lines[1]
            temperature_start = temperature_line.find("t=") + 2
            temperature = float(temperature_line[temperature_start:]) / 1000.0
            return temperature
        else:
            print("Error: Invalid CRC for DS18B20 sensor -", sensor_path)
            return None
    except Exception as e:
        print("Error: Failed to read temperature from DS18B20 sensor -", str(e))
        return None

# Main loop
while True:
    temperature = read_temperature()
    if temperature is not None:
        print("Temperature: {:.2f}°C".format(temperature))
    time.sleep(1)
