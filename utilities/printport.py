
import serial
import time
import struct

ser = serial.Serial('COM9', 115200 , timeout=1)

while 1:
	c = ser.read()
	if c:
		print  hex(ord(c))