from serial import Serial
ser = Serial( "/dev/ttyACM0" , 9600 )

ser.write('f%9d' % 1000 ) #send position, padded to 9 (plus 1 command char)