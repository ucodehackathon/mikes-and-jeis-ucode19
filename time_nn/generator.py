import sys
import os
import random
import re

directory = sys.argv[1]
numSeq = sys.argv[2]
numberOfMovs = sys.argv[3]

count = 0
realMovs = 0
first = 0

isPass = 0
isDribbling = 0
types = ["Dribbling", "Pass-Left", "Pass-Right", "Running", "Shot-Left", "Shot-Right", "Walking"]

namefile = "./exercises/Subject-0" + directory + "-Seq-" + numSeq + "-numMovs-.csv"
file = open(namefile, "w")
namefile2 = "./results/Result-Subject-0" + directory + "-Seq-" + numSeq + "-numMovs-.csv"
file2 = open(namefile2, "w")

while count < int(numberOfMovs):
	size = len(os.listdir("./data/Subject-0" + directory))
	mov = os.listdir("./data/Subject-0" + directory)[random.randint(0, size - 1)]
	path = "./data/Subject-0" + directory + "/" + mov
	print (str(realMovs) + " " + mov)
	print(os.stat(path).st_size)
	sizeFile = os.stat(path).st_size
	while sizeFile < 700:
		mov = os.listdir("./data/Subject-0" + directory)[random.randint(0, size - 1)]
		path = "./data/Subject-0" + directory + "/" + mov
		sizeFile = os.stat(path).st_size
		print (str(realMovs) + " " + mov)
		print(os.stat(path).st_size)
	if isPass == 1:
		while not((re.search('^Running', mov) or re.search('^Walking', mov) and sizeFile > 700)):
			mov = os.listdir("./data/Subject-0" + directory)[random.randint(0, size - 1)]
			path = "./data/Subject-0" + directory + "/" + mov
			sizeFile = os.stat(path).st_size
			print (str(realMovs) + " " + mov)
			print(os.stat(path).st_size)
		isPass = 0
	if isDribbling == 1:
		while not((re.search('^Running', mov) or re.search('^Walking', mov) or re.search('^Dribbling', mov)) and sizeFile > 700):
			mov = os.listdir("./data/Subject-0" + directory)[random.randint(0, size - 1)]
			path = "./data/Subject-0" + directory + "/" + mov
			sizeFile = os.stat(path).st_size
			print (str(realMovs) + " " + mov)
			print(os.stat(path).st_size)
		isDribbling = 0
	if re.search('^Pass', mov):
		isPass = 1
	elif re.search('^Dribbling', mov):
		isDribbling = 1
	elif re.search('^Shot', mov):
		count = int(numberOfMovs)
	f = open("./data/Subject-0" + directory + "/" + mov, "r")
	if not(first == 0):
		f.readline()
	if first == 0:
		file2.write("Dribbling,Pass-Left,Pass-Right,Running,Shot-Left,Shot-Right,Walking,Nothing\n")
	if re.search('^Dribbling', mov):
		s = "1,0,0,0,0,0,0,0"
	elif re.search('^Pass-Left', mov):
		s = "0,1,0,0,0,0,0,0"
	elif re.search('^Pass-Right', mov):
		s = "0,0,1,0,0,0,0,0"
	elif re.search('^Running', mov):
		s = "0,0,0,1,0,0,0,0"
	elif re.search('^Shot-Left', mov):
		s = "0,0,0,0,1,0,0,0"
	elif re.search('^Shot-Right', mov):
		s = "0,0,0,0,0,1,0,0"
	elif re.search('^Walking', mov):
		s = "0,0,0,0,0,0,1,0"
	for x in f:
		file.write(x)
		if not(first == 0):
			file2.write(s + "\n")
		first = 1
	count += 1;
	realMovs += 1;
file.close()
file2.close()
os.rename(namefile, "." + namefile.split(".")[1] + str(realMovs) + ".csv")
os.rename(namefile2, "." + namefile2.split(".")[1] + str(realMovs) + ".csv")