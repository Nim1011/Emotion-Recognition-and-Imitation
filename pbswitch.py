import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
	input_state=GPIO.input(12)
	if(input_state == False):
		print('Button Pressed')
		time.sleep(0.3)
