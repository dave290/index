#meta_index.py
#Reads list of ".ind" files generated by index.py and placed in the Data subdirectory
#where each .ind file contains a batch of scans, and 
#where each .ind file contains GALLON, GALLAT, RA and DEC summaries for a specific batch
#Then creates scatterplot of GLAT vs GLONG

import os
import collections
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig=plt.figure(figsize=(10,6))
ax=plt.axes()
ax.set_title("GLAT vs GLONG")
ax.set_xlabel("GLONG (degrees)")
ax.set_ylabel("GLAT (degrees)")
ax.set_xlim(0,360)
ax.set_ylim(-90,90)
ax.set_xticks([0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360])
ax.set_yticks([-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])

#read filenames and sort by prefix
os.chdir('index_archive')
filelist=os.listdir(".")
filelist.sort()
#print(filelist)

#initialize variables
maxfiles=500;counter=0

#read index file info
for i in filelist:
    GALLON=[0];GALLAT=[0]
    with open(i,'r') as f:
        for line in f:
            linestring=line.split()
            gallon=float(linestring[1])
            gallat=float(linestring[2])
            GALLON.append(gallon)
            GALLAT.append(gallat)
        pass
    f.closed
    True
    GALLON[0]=GALLON[1];GALLAT[0]=GALLAT[1]
    #ax.scatter(GALLON,GALLAT)
    ax.scatter(GALLON,GALLAT,marker=".",label=(i))
    #ax.legend(loc="best")
#end reading files and plot data

#Generate a line passing through galactic latitude of zero degrees
x=[0];y=[0]
for i in range(360):
    x.append(i)
    y.append(0)
ax.scatter(x,y,marker=".")
plt.grid()
plt.show()
exit()