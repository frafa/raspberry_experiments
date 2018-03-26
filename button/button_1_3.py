import RPi.GPIO as GPIO
import time
from random import *
from math import sqrt

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def calc_pi():
	print("calc_pi")
	inside=0
	n=100000
	for i in range(0,n):
		print(i)
		x=random()
		y=random()
		if sqrt(x*x+y*y)<=1:
			inside+=1
	pi=4.0000*inside/n
	print(pi)


if __name__ == '__main__':
	try:		
		print("Start")
		GPIO.add_event_detect(18, GPIO.FALLING)
		calc_pi()
		if GPIO.event_detected(18):
			print('Button pressed')
	finally:
		GPIO.cleanup()

