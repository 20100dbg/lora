import serial
import time

ser = serial.Serial()
ser.braudrate = 9600
ser.port = "/dev/ttyS0"
ser.open()

print(ser.name)
if ser.isOpen():
    print("serial is open!")
else:
    print("problem !")

ser.close()