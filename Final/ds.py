import os
import glob
import time

class DS18B20:
	def __init__(self):
		os.system('modprobe w1-gpio')
		os.system('modprobe w1-therm')
		
	def read_temp_raw(self):
		try:
			base_dir = '/sys/bus/w1/devices/'
			device_folder = glob.glob(base_dir + '28*')[0]
			device_file = device_folder + '/w1_slave'
			f = open(device_file, 'r')
			lines = f.readlines()
			f.close()
			return lines
		except:
			return -1
	
	def readTemperature(self):
		lines = self.read_temp_raw()
		if lines != -1:
			while lines[0].strip()[-3:] != 'YES':
				lines = read_temp_raw()
			equals_pos = lines[1].find('t=')
			if equals_pos != -1:
				temp_string = lines[1][equals_pos+2:]
				temp_c = float(temp_string) / 1000.0
				return round(temp_c, 2)
		else:
			return -1
