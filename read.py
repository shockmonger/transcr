import csv

with open ('/Users/tejas/Documents/CurrentProjects/transcr/test.Pitch', 'r') as file:
    f=file.readlines()

freqlist=[]
for line in f:
	if 'frequency' in line:
		freqlist.append(line)

data=[]
for i in range(len(freqlist)):
	data.append(freqlist[i][28:])

for i in range(len(data)):
	data[i]=data[i].strip()

with open("output.csv", "wb") as fi:
    writer = csv.writer(fi, delimiter=',',quoting=csv.QUOTE_ALL)
    writer.writerows(data)