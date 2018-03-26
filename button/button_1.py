import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#if you do not have the input pin connected to anything, it will 'float'
#In other words, the value that is read in is undefined because it is 
#not connected to anything until you press a button or switch. It will 
#probably change value a lot as a result of receiving mains interference
#
#To get round this, we use a pull up or a pull down resistor. In this 
#way, the default value of the input can be set. It is possible to have 
#pull up/down resistors in hardware and using software. 
#In hardware, a 10K resistor between the input channel and 3.3V 
#(pull-up) or 0V (pull-down) is commonly used. The RPi.GPIO module 
#allows you to configure the Broadcom SOC to do this in software:
#
#GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:	
	while True:
		input_state=GPIO.input(18)
		if input_state == False:
			print("Button pressed")
			time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()
