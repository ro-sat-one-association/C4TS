import urllib
import time

link = "http://localhost/delete_table.php?table="

for i in range(1,6):
	urllib.urlopen(link + str(i))
	time.sleep(0.5)

urllib.urlopen("http://localhost/delete_table.php?table=SHT")
urllib.urlopen("http://localhost/delete_table.php?table=BMP")
urllib.urlopen("http://localhost/delete_table.php?table=DS18")
urllib.urlopen("http://localhost/delete_table.php?table=TSL")
urllib.urlopen("http://localhost/delete_table.php?table=GPS")
urllib.urlopen("http://localhost/delete_table.php?table=time")
