#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

## FUNCOES ##
def GeraMatriz():

 n=int(sys.argv[2])
 fileread=open(sys.argv[1],'r')
 x=[]
 y=[]
 vet=[]
 mat=np.zeros((n+1,n+1), float)
  

 for line in fileread:
  x1,y1=line.split()
  x.append(float(x1))
  y.append(float(y1))



 for ii in xrange(0,n+1):
  for jj in xrange(0,n+1):
   if(ii>=jj):
    somax=0
    for i,j in zip(x,y):
     somax=somax+i**(ii+jj)
    mat.itemset((ii,jj),somax)
 for ii in xrange(0,n+1):
  for jj in xrange(ii,n+1):
   mat.itemset((ii,jj),mat.item(jj,ii))
 for cont in xrange(0,n+1):
  sumxy=0
  for i,j in zip(x,y):
   sumxy=sumxy+(i*j)**cont
  vet.append(sumxy)
 return mat,vet


def Escalona(x,resp):
 lu=np.zeros((n+1,n+1), float)
 resp2=np.zeros(n, float)
 resp2=np.copy(resp)
 lamda=[]
 moddet=0
 op=0
 for tt in xrange(0, n):
  for t in xrange(tt+1,n+1):
   if abs(x.item(tt,tt))<abs(x.item(t,tt)):
    moddet=moddet+1
    y=np.copy(x[tt])
    x[tt]=np.copy(x[t])
    x[t]=np.copy(y)
    segura=resp2[tt]
    resp2[tt]=resp2[t]
    resp2[t]=segura
   op=op+2+n
   lamda.append(x.item(t,tt)/x.item(tt,tt))
   resp2[t]=resp2[t]-lamda[-1]*resp2[tt]
   x[t]=np.copy(x[t]-lamda[-1]*x[tt])
 return x,moddet,lamda,op,resp2

def CalculoDet(x):
 det=1
 for i in xrange(0,n+1):
  det=det*x.item(i,i)
 det=det*(-1)**moddet
 return det



def Substitui(x,resp2):
 y=resp2
 for i in xrange(n,-1,-1):
  j=n
  while (j>i):
   y[i]=y[i]-x.item(i,j)*y[j]
   j=j-1
  y[i]=y[i]/x.item(i,i)
 return y



def Coeficientes(z,y):
 w=np.zeros([n+1], float)
 for tt in xrange(0,n+1):
  for t in xrange(0,n+1):
   w[tt]=np.copy(w[tt]+y[t]*z.item(tt,t))
 return w


## PROGRAMA PRINCIPAL ##

n=int(sys.argv[2])
mat,vet=GeraMatriz()
z=np.copy(mat)
print z
mat,moddet,l,op,resp2=Escalona(mat,vet)
print mat
det=CalculoDet(mat)
print resp2
y=Substitui(mat,resp2)
print "Valores de y: "
print y
w=Coeficientes(z,y)
w=[round(elem,2) for elem in w]
vet=[round(elem,2) for elem in vet]

print "Valores de W: "
print w
print "Valores de vet: "
print vet
print "Os coeficientes são iguais o vetor?"
print w==vet

