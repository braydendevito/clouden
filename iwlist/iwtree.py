import subprocess
import time

mainscan=['sudo python /home/pi/iwlist/iwscan.py>/home/pi/iwlist/mainscan.txt']
sep1=['sudo python /home/pi/iwlist/sep1.py>/home/pi/iwlist/sep1.txt']
sep2=['sudo python /home/pi/iwlist/sep2.py>/home/pi/iwlist/sep2.txt']
sep3=['sudo python /home/pi/iwlist/sep3.py>/home/pi/iwlist/sep3.txt']
sep4=['sudo python /home/pi/iwlist/sep4.py>/home/pi/iwlist/sep4.txt']
sep5=['sudo python /home/pi/iwlist/sep5.py>/home/pi/iwlist/sep5.txt']
sep6=['sudo python /home/pi/iwlist/sep6.py>/home/pi/iwlist/sep6.txt']
sep7=['sudo python /home/pi/iwlist/sep7.py>/home/pi/iwlist/sep7.txt']
sep8=['sudo python /home/pi/iwlist/sep8.py>/home/pi/iwlist/sep8.txt']
htmlgen=['sudo python /home/pi/iwlist/htmlgen.py>/home/pi/templates/main.html']


subprocess.Popen(mainscan, shell=True)

time.sleep(1)

subprocess.Popen(sep1, shell=True)
subprocess.Popen(sep2, shell=True)
subprocess.Popen(sep3, shell=True)
subprocess.Popen(sep4, shell=True)
subprocess.Popen(sep5, shell=True)
subprocess.Popen(sep6, shell=True)
subprocess.Popen(sep7, shell=True)
subprocess.Popen(sep8, shell=True)

time.sleep(1)
subprocess.Popen(htmlgen, shell=True)
