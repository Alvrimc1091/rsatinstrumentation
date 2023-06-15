import time
import picamera

# Initialize the camera
camera = picamera.PiCamera()

# Set camera resolution (optional)
# camera.resolution = (1920, 1080)

# Set camera rotation (optional)
# camera.rotation = 180

# Set camera framerate (optional)
# camera.framerate = 30

# Capture an image
def capture_image(file_path):
    camera.start_preview()
    time.sleep(2)  # Allow camera to stabilize
    camera.capture(file_path)
    camera.stop_preview()
    print("Image captured and saved as:", file_path)

# Main program
if __name__ == '__main__':
    file_path = '/path/to/save/image.jpg'
    capture_image(file_path)
