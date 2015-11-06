import csv
import pandas
import numpy as np
import matplotlib.pyplot as plt

#name=raw_input('Enter file name:')

with open ("/Users/tejas/Documents/CurrentProjects/transcr/test2.Pitch", 'r') as file:
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

data=map(float,data)
data=data[0::2]
datanp= np.asarray(data)

pd = pandas.DataFrame(data)
pd.to_csv("output2.csv",index = False)


# with open("output.csv", "wb") as fi:
#     writer = csv.writer(fi, delimiter=',')
#     writer.writerows(data[i])