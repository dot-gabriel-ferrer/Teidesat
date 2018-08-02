# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 21:17:56 2018

@author: Gabriel
"""

#Simulación de extinción atmosférica teniendo en cuenta la masa de aire que 
#se encuentra entre el objeto que observamos y nosotros

import numpy as np
import matplotlib.pyplot as plt

I=1.
Theta=np.arange(0.1,np.pi/2.+0.001,0.001)
Latmos=np.abs((400./np.sin(Theta)))
Ext=Latmos/np.min(Latmos)*0.16

ax1=plt.axes()
plt.title(r'$Extincio\'n\ atmosfe\'rica$')
ax1.plot(Theta,Ext,'k',Theta+np.pi/2.-0.1,Ext[::-1],'k')
plt.gca().invert_yaxis()
plt.xticks([0,np.pi/2.,np.pi],[r'$0$',r'$90^\circ$',r'$180^\circ$'])
plt.xlim(-0.1,np.pi+0.1)
plt.xlabel(r'$Angulo\ con\ el\ amanecer\ del\ sateelite$')
plt.ylabel(r'$Magnitud\ aparente\ (m)$')

print('############################################\n'
'####Angulo#####################Extincion####\n')
print('0 grados               ',Ext[0])
print('90 grados              ',Ext[-1])
print('180 grados             ',Ext[0],)
print('\n############################################')
