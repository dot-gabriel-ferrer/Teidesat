# -*- coding: utf-8 -*-
"""
Created on Tue Aug 07 19:36:03 2018

@author: Gabriel
"""

#==============================================================================
# Simulacion de Potencia consumida por magnitud aparente buscada
#==============================================================================
import numpy as np
import matplotlib.pyplot as plt

msun=-26.74

ms=np.arange(3,6.6,0.1)

r0=1.496*10**8#Km

rs=400#Km

L0=3.828*10**(26)#W

Ls=L0/2.*(rs**2/r0**2)*10**((ms-msun)/-2.5)
Ms=[]
for i in ms:
    Ms.append(i)
    
fig=plt.figure()
ax=plt.axes()
ax.plot(ms,Ls/10**3)
plt.grid()
plt.xlabel(r'$Magnitud\ Aparente\ (m)$')
plt.ylabel(r'$Potencia\ consumida\ [Kw]$')

plt.title('Potencia Led')

for i in range(0,len(Ls)):
    print 'm=',ms[i],'-----------W=',Ls[i]
    print('=========================================================\n')
