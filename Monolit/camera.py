import os
import time
import subprocess

def getSize(fileobject):
    fileobject.seek(0,2) 
    size = fileobject.tell()
    return size

def test():
	subprocess.call(["rm", "test.jpg"])
	subprocess.call(["raspistill", "-o", "test.jpg"])
	time.sleep(5)
	try:
		file = open('test.jpg', 'rb')
	except IOError:
		return False
		
	if getSize(file) > 1000:
		return True