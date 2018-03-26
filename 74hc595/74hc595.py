import RPi.GPIO as GPIO
import time

# data input
DS = 11
# shift register clock input
SHCP = 12
# memory clock input
STCP = 13

# LED MODE
# Ogni bit rappresenta lo stato che deve assumere il led acceso/spento
#
# es. 0x04 = 00000100 --> terzo led acceso
#     0x55 = 01010101 --> led 1, 3, 5 e 7 accesi

# accensione di un led alla volta da 1 a 8
LED = [0x01,0x02,0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
LED1 = [0x03, 0x03, 0x0C, 0x0C, 0x30, 0x30, 0xC0, 0xC0]
LED2 = [0x00,0x01,0x03,0x06,0x0C,0x18,0x30,0x60,0xC0, 0x80, 0x00]	


def print_msg():
	print ("Avvio programma...")
	print ("Premere Ctrl+C per terminare...")
	
def setup():
	GPIO.setmode(GPIO.BOARD) # utilizzo il numero di pin fisico
	GPIO.setup(DS, GPIO.OUT)
	GPIO.setup(STCP, GPIO.OUT)
	GPIO.setup(SHCP, GPIO.OUT)
	GPIO.output(DS, GPIO.LOW)
	GPIO.output(STCP, GPIO.LOW)
	GPIO.output(SHCP, GPIO.LOW)

# La scrittura dell'informazione nel chip avviene scrivendo un bit 
# alla volta sul canale DS, per ogni bit si manda un segnale sul canale
# SHCP (funzione hc595_in), al termine dell'invio degli 8 dati si manda 
# un segnale sul canale STCP (funzione hc595_out)
#
# dat contiene il byte da inviare al chip
def hc595_in(dat):
    for bit in range(0, 8):
        # 0x80 & (dat << bit) restituisce il bit in posizione bit
        print (0x80 & (dat << bit))
        bit = 0x80 & (dat << bit)
        if (bit == 0):
            GPIO.output(DS, GPIO.LOW)
        else:
            GPIO.output(DS, GPIO.HIGH)
        GPIO.output(STCP, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(STCP, GPIO.LOW)
	
def hc595_out():
    print("-------------")
    GPIO.output(SHCP, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(SHCP, GPIO.LOW)

def loop():
    ledlist=LED2
    while True:
        for i in range(0, len(ledlist)):
            print(ledlist[i])
            hc595_in(ledlist[i])
            hc595_out()
            time.sleep(0.07)
            
        for i in range(len(ledlist)-1, -1, -1):
            print(ledlist[i])
            hc595_in(ledlist[i])
            hc595_out()
            time.sleep(0.07)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	print_msg()
	setup()
	#hc595_in(0x04)
	#hc595_out()
	#time.sleep(5)
	#destroy()
	
	try:
            loop()
	except KeyboardInterrupt:
            destroy()	
