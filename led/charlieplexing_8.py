import RPi.GPIO as GPIO
import time
# per usare il numero di pin
#GPIO.setmode(GPIO.BOARD)
# per usare il numero GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PINS=[16,20,21,26]

H=GPIO.HIGH
L=GPIO.LOW
O=-1

LEDS = [[O,O,H,L],
        [O,L,O,H],
        [O,L,H,O],
        [L,O,H,O],
        [L,H,O,O],
        [H,L,O,O],
        [H,O,L,O],
        [O,H,L,O],
        [O,H,O,L],
        [O,O,L,H]]

def main():
    try:
        while True:
            for led in LEDS:
                for idx, pin in enumerate(led):
                    if pin == O:
                        print("GPIO.setup(",PINS[idx],", GPIO.IN)")
                        GPIO.setup(PINS[idx], GPIO.IN)
                    else:
                        print("GPIO.setup(",PINS[idx],", GPIO.OUT)")
                        print("GPIO.output(",PINS[idx],", ",pin,")")
                        GPIO.setup(PINS[idx], GPIO.OUT)
                        GPIO.output(PINS[idx], pin)
                time.sleep(0.1)
                print("-----------------")
                
    except KeyboardInterrupt:
        pass
    
    finally:
        print("GPIO.cleanup!")
        GPIO.cleanup()
        
if __name__=='__main__':
    main()

