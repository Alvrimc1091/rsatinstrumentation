# ------ PINS ------
# VCC/VIN -> 3.3V (PIN 1)
# GND -> GND (PIN 6)
# SCL -> SCL (PIN 5)
# SDA -> SDA (PIN 3)

import csv
import bmpsensor
import time
import datetime
import pytz
nombre_archivo = 'data_bmp180.csv'
zona_horaria_utc = pytz.utc

# Ciclo de captura y escritura de datos
with open(nombre_archivo, 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Hora_UTC' ,'Temp', 'Pressure', 'Altitud'])  # Escribir encabezados de columna

    while True:
        temp, pressure, altitude = bmpsensor.readBmp180()
        hora_actual = datetime.datetime.now(tz=zona_horaria_utc).strftime('%H%M%S')

        escritor_csv.writerow([hora_actual, temp, pressure, altitude])
        archivo_csv.flush()  # Vaciar el búfer y asegurarse de que se escriban los datos en el archivo

        time.sleep(1)  # Esperar 1 segundo antes de la siguiente captura
