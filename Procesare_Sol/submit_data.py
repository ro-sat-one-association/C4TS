import urllib
import time

delay = 5 #cate secunde astept intre
		  #introducerea datelor

f = open('date.txt')

counter = 1
t1 = "http://localhost/submit.php?table=1&v1="
t2 = "http://localhost/submit.php?table=2&v1="
t3 = "http://localhost/submit.php?table=3&v1="
t4 = "http://localhost/submit.php?table=4&v1="
t5 = "http://localhost/submit.php?table=5&v1="

for line in f:
	if counter == 1:
		t1 += str(line).rstrip()
		
	if counter == 2:
		t1 += "&v2="
		t1 += str(line).rstrip()
		urllib.urlopen(t1)
		t1 = "http://localhost/submit.php?table=1&v1="
		
	if counter == 3:
		t2 += str(line).rstrip()
		
	if counter == 4:
		t2 += "&v2="
		t2 += str(line).rstrip()
		urllib.urlopen(t2)
		t2 = "http://localhost/submit.php?table=2&v1="
	
	if counter == 5:
		t3 += str(line).rstrip()
		
	if counter == 6:
		t3 += "&v2="
		t3 += str(line).rstrip()
		urllib.urlopen(t3)
		t3 = "http://localhost/submit.php?table=3&v1="

	if counter == 7:
		t4 += str(line).rstrip()
		
	if counter == 8:
		t4 += "&v2="
		t4 += str(line).rstrip()
		urllib.urlopen(t4)
		t4 = "http://localhost/submit.php?table=4&v1="
		
	if counter == 9:
		t5 += str(line).rstrip()
		
	if counter == 10:
		t5 += "&v2="
		t5 += str(line).rstrip()
		urllib.urlopen(t5)
		t5 = "http://localhost/submit.php?table=5&v1="
	
	counter = counter + 1
	
	if not line.strip():
		time.sleep(delay)
		counter = 1
		
