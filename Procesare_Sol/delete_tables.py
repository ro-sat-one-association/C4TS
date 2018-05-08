import urllib
import time

link = "http://localhost/delete_table.php?table="

for i in range(1,6):
	urllib.urlopen(link + str(i))
	time.sleep(0.5)

