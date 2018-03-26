import RPi.GPIO as GPIO
import time

#utilizzo il numeor di pin logico
GPIO.setmode(GPIO.BCM)

def RCtime(RCpin):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
	time.sleep(0.1)
	
	GPIO.setup(RCpin, GPIO.IN)
	while(GPIO.input(RCpin)==GPIO.LOW):
		reading+=1
	
	return reading

def destroy():
	GPIO.cleanup()


if __name__ == '__main__':
	try:
		while True:
			print(RCtime(18))

	except KeyboardInterrupt:
            destroy()	
	
