import csv
import pandas

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

pd = pandas.DataFrame(data)
pd.to_csv("output.csv")


# with open("output.csv", "wb") as fi:
#     writer = csv.writer(fi, delimiter=',')
#     writer.writerows(data[i])