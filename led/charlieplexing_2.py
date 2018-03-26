import RPi.GPIO as GPIO
import time
# per usare il numero di pin
#GPIO.setmode(GPIO.BOARD)
# per usare il numero GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print ("LED 1 on")
GPIO.setup(20, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
time.sleep(1)
print ("LED 2 on")
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)
