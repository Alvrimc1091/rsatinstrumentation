import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--width", type=int, help="Ancho")
parser.add_argument("-a", "--altura", type=int, help="Alto")

args = parser.parse_args()

os.system("libcamera-jpeg -o IMAGEN.jpg --width "+str(args.width)+" --heigh "+str(args.altura))
