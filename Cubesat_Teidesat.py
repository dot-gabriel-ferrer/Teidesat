# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 11:22:05 2018

@author: Gabriel
"""

import Earth_atmosphere_model as Atmos
import matplotlib.pyplot as plt
import numpy as np

#==============================================================================
# BALISTIC COEFFICIENT (BC).....BC=m/(CD*S)
#                               m==mass
#                               CD==drag coefficient
#                               S==Front surface
#==============================================================================
T,P,ro,C,h=Atmos.Atmosphere()

Cd=0.8
m=1.#Kg
S=np.sqrt(2)*0.01#m2
BC=m/Cd/S#kg/m2

#==============================================================================
# Rozamiento con la atmosfera
# Fdrag.....Fdrag=1/2 * ro * v**2 * Cd * S
#
# Aceleracion de frenado con la atmosfera
# adrag.....adrag=1/2 * ro * v**2 * Cd* S / m
#
# Suponemos adrag(0)=1/2*ro(0)*viss**2*Cd*S/m
#
# Velocidad del satelite
# vsat=viss-adrag*t
#   viss==velocidad estacion espacial internacional
#   t== tiempo desde el lanzamiento de la iss
#==============================================================================
'''
Revisar los datos, datos de prueba
'''


ro=0.000001
viss=7660#m/s
t=np.arange(0,10000,0.5)
a0=1./2*ro*viss**2/BC
v0=viss
V=[]
A=[]
for i in range(len(t)):
    if v0>=0.:
        V.append(v0)
        A.append(a0)
        v0=v0-a0*t[i]
        a0=1/2.*ro*V[i]**2/BC
    
plt.clf()   
plt.figure(1)
ax1=plt.axes()
ax1.plot(V,h)