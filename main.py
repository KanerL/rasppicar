import serial
import RPi.GPIO as GPIO
import time

LedPin = 11    # pin11
ser=serial.Serial("/dev/ttyACM0",9600)  #change ACM number as found from ls /dev/tty/ACM*
ser.baudrate=9600
def setup():
   GPIO.setmode(GPIO.BOARD)       # Set the board mode to numbers pins by physical location
   GPIO.setup(LedPin, GPIO.OUT)   # Set pin mode as output
   GPIO.output(LedPin, GPIO.HIGH) # Set pin to high(+3.3V) to off the led

def blink():
           print('led on')
           GPIO.output(LedPin, GPIO.LOW)   # led on
           time.sleep(1.0)                 # wait 1 sec
           print('led off')
           GPIO.output(LedPin, GPIO.HIGH)  # led off
           time.sleep(1.0)                 # wait 1 sec


setup()
while True:
   serialmessage = ser.readline()
   print("serial message is " + serialmessage)
   if serialmessage == "hello":
       print("message recieved")
       blink()