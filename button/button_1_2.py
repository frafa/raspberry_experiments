import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:	
	while True:
		#The wait_for_edge() function is designed to block execution of your program until an edge is detected
		# wait 5 sec. before exit
		# wait for button pressed event
		input_state=GPIO.wait_for_edge(18, GPIO.FALLING, timeout=5000)
		if input_state is None:
			print("Timeout")
		else:
			print("Button pressed")

except KeyboardInterrupt:
	GPIO.cleanup()
