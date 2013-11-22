import os
from pandas import Series,DataFrame
import pandas as pd

def getdata(source):
    data=[]
    file=open(source)
    for line in file:
        line=line.split()
        line[0]=float(line[0])
        line[5]=int(line[5])
        data.append([line[0],line[5]])
    file.close()
    return data
           
data=getdata('lbl-tcp-3.tcp')
frame=DataFrame(data,
                columns=['timestamp','bytes'])

rate=[]
rate.append(0)
time=1
t=0
for a in data:
    if a[0]<time:
        t=t+a[1]
    else:
        time+=1
        rate.append(t/1024)
        t=a[1]


out=open('rate.dat','w')
out.write('\n'.join(map(lambda x:str(x),rate)))
out.close()
