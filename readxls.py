#-*-coding:utf-8-*-
#! filename:readxls.py

import csv

#get data from excel 
trace=[]
flow=[]
with open("netflow1.xls","r") as f:
    reader=csv.reader(f,dialect="excel")
    for row in reader:
        flow.append(row)
flow=flow[2:]

#formatting
#trace中每项包括的内容分别是:
#trace编号,源IP,目的IP,IP协议,目的协议端口,比特流(kbit/s)
#帧流量(Frame/s),session数,源协议端口,以太网协议

for i in flow:
    i=i[0].split(" \t")
    j=i[0:8]+[i[10]]+[i[11]]
    j[0]=int(j[0])
    j[3]=j[3].strip()
    j[5]=float(j[5])
    j[6]=float(j[6])
    j[7]=int(j[7])
    trace.append(j)

#calculate the average rate during this 10s
rate=0
for i in trace:
    rate+=i[5]
print rate






