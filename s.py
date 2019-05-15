import time

import serial

port = 'COM3'


ard = serial.Serial(port,9600,timeout=5)
while True:
    # Serial write section
    setTempCar1 = 'r100'
    print ("Python value sent: ")
    print (setTempCar1)
    ard.write(setTempCar1.encode())
    time.sleep(6) # with the port open, the response will be buffered
                  # so wait a bit longer for response here
    msg = ard.read(ard.inWaiting())  # read everything in the input buffer
    print(msg)
    if msg == b'ready':
        ard.write('f010'.encode())
        ard.write('b010'.encode())

