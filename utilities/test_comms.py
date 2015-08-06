
import serial
import time
import struct
import binascii

ser = serial.Serial('COM6', 9600 , timeout=0.1)

fob = open("putty.log",'r')
sendstring = "A"

def get_file_packet():
	packet = fob.read(209)
	return packet

def get_micro_packet():
	print ""
	print "sending"
	ser.write(sendstring)
	print "recieving"
	packet = ""
	while 1:
		thischar = ser.read();
		if not thischar:
			break
		packet = packet + thischar
	return packet

def parse_packet(packet):
	print "size: " + str(len(packet))
	if len(packet) > 30:
		print "battery voltage: " + str(struct.unpack('>h', packet[26:28] )[0]*0.1)
		print "clt: " + str( (struct.unpack('>h', packet[22:24] )[0] - 320)  *0.05555 )
		print "rpm: " + str( (struct.unpack('>H', packet[6:8] )[0] ) )
	else:
		print packet

while 1:
	packet = get_micro_packet()
	if packet:
		#print ":".join("{:02x}".format(ord(c)) for c in packet)
		parse_packet(packet)

	time.sleep(1)