import serial
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.flushInput()

while True:
    if ser.inWaitin()>0:
        inputValue = ser.read(1)
        print(inputValue)