#! /usr/bin/env python
#! -*-coding:utf-8 -*-
"""
Usage:
python rate.py [time interval]
"""
import os
from pandas import Series,DataFrame

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

delta=int(input('Time interval /s:'))
data=getdata('lbl-tcp-3.tcp')
frame=DataFrame(data,
                columns=['timestamp','bytes'])

rate=[]
rate.append(0)
t=0
time=delta
for a in data:
    if a[0]<time:
        t=t+a[1]
    else:
        rate.append(t/1024/delta)
        time+=delta
        t=a[1]


out=open('rate_'+str(delta)+'s'+'.dat','w')
out.write('\n'.join(map(lambda x:str(x),rate)))
out.close()
