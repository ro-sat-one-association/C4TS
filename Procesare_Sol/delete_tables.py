import urllib
import time


host = "localhost"
pass_script = "pass"

link = "http://" + host + "/delete_table.php?pass=" + pass_script + "&table="

for i in range(1,6):
	urllib.urlopen(link + str(i))
	time.sleep(0.5)

urllib.urlopen("http://" + host + "/delete_table.php?pass=" + pass_script + "&table=SHT")
urllib.urlopen("http://" + host + "/delete_table.php?pass=" + pass_script + "&table=BMP")
urllib.urlopen("http://" + host + "/delete_table.php?pass=" + pass_script + "&table=DS18")
urllib.urlopen("http://" + host + "/delete_table.php?pass=" + pass_script + "&table=TSL")
urllib.urlopen("http://" + host + "/delete_table.php?pass=" + pass_script + "&table=GPS")
urllib.urlopen("http://" + host + "/delete_table.php?pass=" + pass_script + "&table=time")
