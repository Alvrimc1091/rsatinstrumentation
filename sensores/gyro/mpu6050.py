import smbus2

# MPU-6050 registers
MPU6050_ADDR = 0x68
MPU6050_ACCEL_XOUT_H = 0x3B
MPU6050_PWR_MGMT_1 = 0x6B

# Create an SMBus object
bus = smbus2.SMBus(1)

# Initialize the MPU-6050 sensor
def initialize_sensor():
    bus.write_byte_data(MPU6050_ADDR, MPU6050_PWR_MGMT_1, 0)

# Read the raw accelerometer data from the MPU-6050
def read_accelerometer_data():
    accel_x = read_word_2c(MPU6050_ACCEL_XOUT_H)
    accel_y = read_word_2c(MPU6050_ACCEL_XOUT_H + 2)
    accel_z = read_word_2c(MPU6050_ACCEL_XOUT_H + 4)
    return accel_x, accel_y, accel_z

# Read a 16-bit signed value from the MPU-6050
def read_word_2c(reg):
    high = bus.read_byte_data(MPU6050_ADDR, reg)
    low = bus.read_byte_data(MPU6050_ADDR, reg + 1)
    value = (high << 8) + low
    if value >= 0x8000:
        value = -((65535 - value) + 1)
    return value

# Main program
if __name__ == '__main__':
    # Initialize the sensor
    initialize_sensor()
    
    # Read and display accelerometer data
    accel_x, accel_y, accel_z = read_accelerometer_data()
    print("Accelerometer Data:")
    print("X: {}".format(accel_x))
    print("Y: {}".format(accel_y))
    print("Z: {}".format(accel_z))

