#index.py
#python index.py
#Read list of ast (or kel) files placed in the Data subdirectory
#Retrieve the GLONG, GLAT, RA and DEC from each file
#Write this data to file "20-09-24.ind"
#Create scatterplot of GLAT vs GLONG 

import os
import collections

#read filenames and sort by prefix
os.chdir('data')
filelist=os.listdir(".")
filelist.sort()
datename=filelist[0]
datename=datename[0:-11]+".ind"

#initialize variables
maxfiles=1000;counter=0
date=[999];colon=[999];GALLON=[999];GALLAT=[999];RA=[999];DEC=[999]
for i in range(maxfiles):
    date.append(999)
    GALLON.append(999)
    GALLAT.append(999)
    RA.append(999)
    DEC.append(999)

#read header info
for i in filelist:
    date[counter]=i[0:15]
    with open(i,'r') as f:
        for line in f:
            linestring=line.split()
            if linestring[1]=="File:":   #this is format for ast files
                datestring=linestring[2]
            if linestring[1]=="FILE":     #this is format for kel files
                datestring=linestring[2]
            if linestring[1]=="AZ":
                azimuth=linestring[3]
            if linestring[1]=="EL":
                elevation=linestring[3]
            if linestring[1]=="RA":
                coordinate=linestring[3]
                for j in range(8):
                    if coordinate[j]==":":
                        colon.append(j)
                hours=float(coordinate[0:colon[1]])
                minutes=float(coordinate[colon[1]+1:colon[2]])
                seconds=float(coordinate[colon[2]+1:])
                hours=hours+minutes/60.0+seconds/3600.0
                hours=float(round(hours,2))
                RA[counter]=hours
                colon=[999]
            if linestring[1]=="DEC":
                coordinate=linestring[3]
                for j in range(8):
                    if coordinate[j]==":":
                        colon.append(j)
                degrees=float(coordinate[0:colon[1]])
                minutes=float(coordinate[colon[1]+1:colon[2]])
                seconds=float(coordinate[colon[2]+1:])
                degrees=degrees+minutes/60.0+seconds/3600.0
                degrees=float(round(degrees,2))
                DEC[counter]=degrees
                colon=[999]
            if linestring[1]=="GALLON":
                coordinate=linestring[3]
                for j in range(8):
                    if coordinate[j]==":":
                        colon.append(j)
                degrees=float(coordinate[0:colon[1]])
                minutes=float(coordinate[colon[1]+1:colon[2]])
                seconds=float(coordinate[colon[2]+1:])
                degrees=degrees+minutes/60.0+seconds/3600.0
                degrees=float(round(degrees,2))
                GALLON[counter]=degrees
                colon=[999]
            if linestring[1]=="GALLAT":
                coordinate=linestring[3]
                for j in range(8):
                    if coordinate[j]==":":
                        colon.append(j)
                degrees=float(coordinate[0:colon[1]])
                minutes=float(coordinate[colon[1]+1:colon[2]])
                seconds=float(coordinate[colon[2]+1:])
                degrees=degrees+minutes/60.0+seconds/3600.0
                degrees=float(round(degrees,2))
                GALLAT[counter]=degrees
                colon=[999]
    f.closed
    True
    counter=counter+1

#print data to terminal window
print(" ")
print("DATE                   GALLON     GALLAT    RA           DEC")
for i in range(counter):
    print("{: >10} {: >10} {: >10} {: >10} {: >10}".format(date[i],str(GALLON[i]),str(GALLAT[i]),str(RA[i]),str(DEC[i])))  
print("Number of .kel files ",counter)
print(" ")

#open index file and append filename, GLONG, GLAT, RA and DEC
os.chdir("..")
with open(datename,'w') as g:
    for i in range(counter):
        g.write("{: >10} {: >10} {: >10} {: >10} {: >10}".format(date[i],str(GALLON[i]),str(GALLAT[i]),str(RA[i]),str(DEC[i])))
        g.write("\n")
g.closed
True

#deque lists to remove last (max-counter) items; must do before plotting
date_dequed=collections.deque(date)
GALLON_dequed=collections.deque(GALLON)
GALLAT_dequed=collections.deque(GALLAT)
RA_dequed=collections.deque(RA)
DEC_dequed=collections.deque(DEC)
for i in range(maxfiles-counter+1):
    date_dequed.remove(999)
    GALLON_dequed.remove(999)
    GALLAT_dequed.remove(999)
    RA_dequed.remove(999)
    DEC_dequed.remove(999)
date=list(date_dequed)
GALLON=list(GALLON_dequed)
GALLAT=list(GALLAT_dequed)
RA=list(RA_dequed)
DEC=list(DEC_dequed)

#plot data
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
fig=plt.figure(figsize=(10,6))
ax=plt.axes()

#Generate a line passing through galactic latitude of zero degrees
x=[0];y=[0]
for i in range(360):
    x.append(i)
    y.append(0)
ax.scatter(x,y,marker=".")

ax.set_title(datename[0:8])
#ax.set_title(datename[0:8]+" EL="+elevation+" AZ="+azimuth)
#ax.set_xlabel("GLONG (degrees)")
#ax.set_ylabel("GLAT (degrees)")
ax.set_xlim(0,360)
ax.set_ylim(-90,+90)
ax.scatter(GALLON,GALLAT,marker=".")
plt.show()
exit()