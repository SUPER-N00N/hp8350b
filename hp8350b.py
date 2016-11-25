#!/usr/bin/python
import serial

class HP8350B:
	GPIB_ADDRESS = 19 #default for HP8350
	fd = None
	def __init__(self, gpib_path):
		splitted_path = gpib_path.split('::');
		if splitted_path[0] == "PROLOGIX":
		#	self.fd = serial.Serial(splitted_path[1], baudrate=921600, timeout=0.5);
			self.fd = serial.Serial(splitted_path[1], baudrate=9600, timeout=0.5);
			self.fd.write("++read_tmo_ms 400 \n")
			self.GPIB_ADDRESS = int(splitted_path[-1]);
		else:
			print("penis!\n");
	
	def cmd(self, cmd):
		self.fd.write("++addr %d\n" %self.GPIB_ADDRESS)
		self.fd.write(cmd + "\r\n");
		result = []
		c = 10
		while c > 0:
			lines = self.fd.readlines()
			if len(lines) > 0:
				c = 0
				for c_0 in lines:
					result.append(c_0)
			c-=1
		return result
	def write(self, cmd):
		self.fd.write("++addr %d\n" %self.GPIB_ADDRESS)
		self.fd.write(cmd + "\n")
		return
							
	def frq_start(self, frq):
		return self.cmd("FA" + frq + "\r\n");
	def frq_stop(self, frq):
		return self.cmd("FB" + frq + "\r\n");
	def dBm(self, dbm):
		return self.cmd("PL" + dbm + "DM\r\n");
	def setSweepTime(self, dbm):
		return self.cmd("ST" + dbm + "MS\r\n");
	
