# seek.py
# Lists kel files containing data within specified galactic longitude and latitude windows
# python seek.py -glongval 55 -glongwin 2 -glatval 15 -glatwin 2
# 12/6/2022

import os
import collections

import argparse
parser = argparse.ArgumentParser(description='seek.py')
parser.add_argument("-glongval", "--glongval", help="glongval in degrees", type=float)
parser.add_argument("-glongwin", "--glongwin", help="glongwin in degrees", type=float)
parser.add_argument("-glatval", "--glatval", help="glatval in degrees", type=float)
parser.add_argument("-glatwin", "--glatwin", help="glatwin in degrees", type=float)
args = parser.parse_args()
GLONG_VAL=args.glongval
GLONG_WIN=args.glongwin
GLAT_VAL=args.glatval
GLAT_WIN=args.glatwin
A=GLONG_VAL-0.5*GLONG_WIN
B=GLONG_VAL+0.5*GLONG_WIN
C=GLAT_VAL-0.5*GLAT_WIN
D=GLAT_VAL+0.5*GLAT_WIN
print("GLONG RANGE",A,B)
print("GLAT  RANGE",C,D)

#read filenames and sort by prefix
os.chdir('data')
filelist=os.listdir(".")
filelist.sort()

#read index file info
for i in filelist:
    GALLON=[0];GALLAT=[0]
    with open(i,'r') as f:
        for line in f:
            linestring=line.split()
            kel_file=str(linestring[0])
            gallon=float(linestring[1])
            gallat=float(linestring[2])
            if (gallon>A) and (gallon<B) and (gallat>C) and (gallat<D):
                print(kel_file,gallon,gallat)
            #endif
        pass
    f.closed
    True
exit()