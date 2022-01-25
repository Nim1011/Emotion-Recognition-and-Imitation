import serial
import time

def serialcom(str):
	print(str)
	ser = serial.Serial('/dev/ttyACM0', 115200)
	time.sleep(2)
	if ser.isOpen():
    		print("Port Open")
	if(str == 'happiness'):
		print (ser.write("happy\n"))
	elif(str == 'sadness'):
		print (ser.write("sad\n"))
	elif(str == 'anger'):
                print (ser.write("anger\n"))
	elif(str == 'contempt'):
                print (ser.write("contempt\n"))
	elif(str == 'neutral'):
                print (ser.write("neutral\n"))
	elif(str == 'fear'):
                print (ser.write("fear\n"))
	elif(str == 'disgust'):
                print (ser.write("disgust\n"))
	elif(str == 'surprise'):
                print (ser.write("surpise\n"))
	
	else:
		print (ser.write("None\n"))

	ser.close()

