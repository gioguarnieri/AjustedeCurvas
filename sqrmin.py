#!/usr/bin/env python

import sys
import numpy as np


def Ler(x,y):
 fileread=open(sys.argv[1],'r')
 for line in fileread:
  x1,y1=line.split()
  x.append(float(x1))
  y.append(float(y1))
 return x,y

def fitlin(x,y):
 somaxquad=0
 somay=0
 somaxy=0
 somax=0
 for i,j in zip(x,y):
  somaxquad=somaxquad+i**2
  somay=somay+j
  somaxy=somaxy+i*j
  somax=somax+i
 a0=(somaxquad*somay-somaxy*somax)/(len(x)*somaxquad-somax**2)
 a1=(len(x)*somaxy-somax*somay)/(len(x)*somaxquad-somax**2)
 return a0,a1

x=[]
y=[]

x,y=Ler(x,y)
print "Valores de X e Y:"
print x,y 

a0,a1=fitlin(x,y)
print "a0: ", a0, "a1: ", a1
