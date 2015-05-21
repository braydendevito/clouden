with open ('/home/pi/iwlist/mainscan.txt', 'r') as infile:
	data = infile.read()
mylist = data.split("\n")
print (mylist[1])
