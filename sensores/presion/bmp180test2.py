import smbus
import time

# BMP180 Registers
BMP180_ADDR = 0x77
BMP180_CTRL_MEAS = 0xF4
BMP180_ADC_MSB = 0xF6
BMP180_ADC_LSB = 0xF7

# Calibration coefficients
AC1 = 0xAA
AC2 = 0xAC
AC3 = 0xAE
AC4 = 0xB0
AC5 = 0xB2
AC6 = 0xB4
B1 = 0xB6
B2 = 0xB8
MB = 0xBA
MC = 0xBC
MD = 0xBE

# Read a 16-bit signed value from the BMP180
def read_short(address):
    msb = bus.read_byte_data(BMP180_ADDR, address)
    lsb = bus.read_byte_data(BMP180_ADDR, address + 1)
    value = (msb << 8) + lsb
    if value >= 0x8000:
        value = -((65535 - value) + 1)
    return value

# Read the calibration coefficients from the BMP180
def read_calibration():
    calibration = {}
    calibration['ac1'] = read_short(AC1)
    calibration['ac2'] = read_short(AC2)
    calibration['ac3'] = read_short(AC3)
    calibration['ac4'] = read_short(AC4)
    calibration['ac5'] = read_short(AC5)
    calibration['ac6'] = read_short(AC6)
    calibration['b1'] = read_short(B1)
    calibration['b2'] = read_short(B2)
    calibration['mb'] = read_short(MB)
    calibration['mc'] = read_short(MC)
    calibration['md'] = read_short(MD)
    return calibration

# Read the uncompensated temperature from the BMP180
def read_temperature():
    bus.write_byte_data(BMP180_ADDR, BMP180_CTRL_MEAS, 0x2E)
    time.sleep(0.005)
    msb = bus.read_byte_data(BMP180_ADDR, BMP180_ADC_MSB)
    lsb = bus.read_byte_data(BMP180_ADDR, BMP180_ADC_LSB)
    value = (msb << 8) + lsb
    return value

# Read the uncompensated pressure from the BMP180
def read_pressure(oss=0):
    bus.write_byte_data(BMP180_ADDR, BMP180_CTRL_MEAS, 0x34 + (oss << 6))
    time.sleep(0.014 + (0.008 * (1 << oss)))
    msb = bus.read_byte_data(BMP180_ADDR, BMP180_ADC_MSB)
    lsb = bus.read_byte_data(BMP180_ADDR, BMP180_ADC_LSB)
    xlsb = bus.read_byte_data(BMP180_ADDR, BMP180_ADC_LSB + 1)
    value = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - oss)
    return value

# Calculate the true temperature from the uncompensated temperature value
def calculate_temperature(ut, calibration):
    x1 = ((ut - calibration['ac6']) * calibration['ac5']) >> 15
    x2 = (calibration['mc'] << 11) // (x1 + calibration['md'])
    b5 = x1 + x2
    t = (b5 + 8) >> 4
    return
