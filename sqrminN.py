#!/usr/bin/env python

import sys
import numpy as np

n=float(sys.argv[2])
fileread=open(sys.argv[1],'r')
mat=np.zeros((n+1,n+1), float)
x=[]
y=[]
for line in fileread:
 x1,y1=line.split()
 x.append(float(x1))
 y.append(float(y1))
cont=0
while(cont<=2*n):
 somax=0
 somaxy=0
 for i,j in zip(x,y):
  somax=somax+i**cont
  somaxy=(i*j)**cont
 cont2=cont
 cont3=0
 while(cont2>=0):
  mat.itemset((cont2,cont3),somax)
  cont3=cont3+1
  cont2=cont2-1
 cont=cont+1
 print mat

print mat
