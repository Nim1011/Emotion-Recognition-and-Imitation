import time
import picamera
import facedetect_pi
camera = picamera.PiCamera()

def load_image():
	    camera.resolution = (1024, 768)
	    camera.start_preview()
	    camera.capture('capture.jpg')
	    facedetect_pi.emodet()


