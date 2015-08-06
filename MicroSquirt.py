

import serial
import struct

def parsetype(dtype):
	tflag = -1
	if dtype == 'S16':
		tflag = '>h'
	elif dtype == 'U16':
		tflag = '>H'
	elif dtype == 'U08':
		tflag = '>B'
	elif dtype == 'U8':
		tflag = '>B'
	elif dtype == 'U32':
		tflag = '>L'
	elif dtype == 'S32':
		tflag = '>l'
	else:
		print "Unknown datatype: ", dtype
		raise
	return tflag

def splitline(dataline):
	return dataline.split()

def typesize(dtype):
	if dtype == 'S16':
		size = 2
	elif dtype == 'U16':
		size = 2
	elif dtype == 'U08':
		size = 1
	elif dtype == 'U8':
		size = 1
	elif dtype == 'U32':
		size = 4
	elif dtype == 'S32':
		size = 4
	else:
		print "Unknown datatype: ", dtype
		raise
	return size

def parsewithkey(packet, datumkey):
	dtype = datumkey[1]
	index = int(datumkey[2])
	scale = float(datumkey[3])
	translate = int(datumkey[4])
	size = typesize(dtype)

	tflag = parsetype(dtype)
	if scale != 0:
		outputval = (struct.unpack(tflag, packet[index:index+size] )[0] + translate) * scale
	else:
		outputval = struct.unpack(tflag, packet[index:index+size] )[0]
	return outputval


class MicroSquirt:

	def __init__(self, portlocation , minpacketlength = 100, baudrate = 115200, mstimeout = 0.1, filename = "dataformat.txt"):
		try:
			self.port = serial.Serial(portlocation, baudrate , timeout = mstimeout)
			print "Serial port opened"
			self.logging = False
			self.minpacketlength = minpacketlength
		except:
			print "Could not open serial port at location: ", portlocation
			raise
		self.builddatakey(filename)

	def set_logging(self,tflag):
		self.logging = tflag

	def builddatakey(self,filename):
		try:
			fileobject = open(filename, 'r')
		except:
			print "Could not open file: ", filename
		print "Creating datakey"

		self.datakey = []
		for line in fileobject:
			self.datakey.append( splitline( line ) )
		print "Data key length: ", len(self.datakey)

	def get_packet(self):
		self.port.write("A")
		packet = ""
		while 1:
			thischar = self.port.read();
			if not thischar:
				break
			packet = packet + thischar
		return packet

	def parse_packet(self, packet):
		print "Size: " + str(len(packet))
		if len(packet) > self.minpacketlength:
			packetcontents = []
			for dkey in self.datakey:
				value = parsewithkey(packet, dkey)
				packetcontents.append(value)
			return packetcontents
		else:
			print "Packet is too short: ", packet

	def get_data(self):
		packet = self.get_packet()
		packetcontents = self.parse_packet(packet)
		print packetcontents
