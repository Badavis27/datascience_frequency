#PinkPanther
#9-11-17
#challenge 1
#https://pythonprogramming.net/reading-csv-files-python-3/
#Lecture notes


from __future__ import division
import numpy as np
import matplotlib.pyplot as mplot
from collections import defaultdict

file=open("PinkPanther_ch1.csv", "r")
data=file.read()
data=data.split("\n")
data.pop()


x=[]
y=[]

for index in range(len(data)):
    data[index]=data[index].split(",")
    #print index
    try:
        data[index]=np.float32(data[index])
        
    except:
        print (data[index])
        print ("index", index)

M,A,F=zip(*data)
Sum = 0
for row in data:
    #Sum += row[1]
    #AA =Sum/ 11049
    F=row[2]
    if(F<72):
        M=row[0]
        A=row[1]
        x.append(M)
        y.append(A)



dct={}


YY=[]
XX=[]


for row in data:
    F=row[2]
    if(F<72):
        M=row[0]
        A=row[1]
        try: 
            dct[M].append(A)
        except:
            dct[M]=[]
            dct[M].append(A)
print dct
for key, value in dct.items():
    XX.append(key)
    avg= np.mean(value)
    YY.append(avg)
Temp=zip(XX,YY)
Temp= sorted(Temp)
XX,YY=zip(*Temp)            
"""dct={M:A}
        for key, value in dct.items():
            print (key,"=", value)
            i = key
            if i in M and key:
                
                count +=1
                Summ +=value
                YY.append(Summ/count)
"""
#avg = defaultdict(lambda :{'count' : 0, 'Summ' : 0})
#for row in data:
    #F=row[2]
    #M=row[0]
    #A=row[1]
    #if(F<72):
        #dct={M:A} 
        #for ke, va in dct.items():
            #for v in va [:-1]:
                #avg = v/va[-1] 
                #print key, avg
            
            
                
            


mplot.xlabel("milliseconds")
mplot.ylabel("amplitude")
mplot.scatter(x, y)
mplot.plot(XX,YY, color= "red")
mplot.show()