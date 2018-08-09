# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 21:17:56 2018

@author: Gabriel
"""

#Simulación de extinción atmosférica teniendo en cuenta la masa de aire que 
#se encuentra entre el objeto que observamos y nosotros

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib as mpl
from matplotlib.ticker import LinearLocator, FormatStrFormatter
plt.clf()
plt.clf()
plt.clf()
#==============================================================================
#Suponemos una altura fija de 400Km, y suponemos que la distancia del
#satelite hasta nosotros varía solo en ángulo con respecto al suelo
#
#La altura de Izaña es de 2390m (h), el radio de la Tierra es de 6371Km (R). 
#Usando el Teorema de Pitágoras podemos obtener la distancia desde nosotros hasta
#el horizonte (d).
#
#   d=sqrt((R+h)^2-R^2)
#
#con lo que se obtiene una distancia del horizonte desde Izaña de 174.52Km
#
#Esto hace que el rango de ángulos donde se podrá ver el satélite es desde los 
#   66.42 grados hasta los 113.57 grados. Aproximadamente
#
# ESTE CALCULO HA SIDO REALIZADO SUPONIENDO UNA CURVATURA TERRESTRE INFIMA DEBIDO
# A LAS DISTANCIAS QUE SE MANEJAN, QUE NO CAMBIAN DEMASIADO EL RESULTADO AL TENER 
# EN CUENTA LA CURVATURA
#==============================================================================

I=1.
Theta=np.arange(0.1,np.pi/2.+0.001,0.001)
Latmos=np.abs((400./np.sin(Theta)))
Ext=Latmos/np.mean(Latmos)*0.16

#==============================================================================
# Gráfico de resultados de extinccion
#==============================================================================

ax1=plt.axes()
plt.title(r'$Extincio\'n\ atmosfe\'rica\ ZENIT$')
ax1.plot(Theta,Ext,'k',Theta+np.pi/2.-0.1,Ext[::-1],'k')
plt.ylabel(r'$Magnitud\ aparente\ (m)$')
plt.xlabel(r'$Angulo\ con\ el\ amanecer\ del\ satelite$')
plt.gca().invert_yaxis()
plt.twinx()
plt.gca().invert_yaxis()
plt.yticks((np.array([1,2,3,4,5,6,7,8,9,10])*0.1).tolist(),np.array([1,2,3,4,5,6,7,8,9,10]))
plt.ylabel(r'$Masas\ de\ aire$')
plt.xticks([0,np.pi/2.,np.pi],[r'$0$',r'$90^\circ$',r'$180^\circ$'])
plt.xlim(-0.1,np.pi+0.1)
#==============================================================================
# Plot del rango visible real del satélite, y ángulos a tener en cuenta para definit
# la potencia máxima del led necesaria para observarlo
#
# Hay que tener en cuenta que en Izaña la presion atmosférica es un 70% de la presion
# a nivel del mar, por lo que tendremos menos masa de aire encima y menor extinción
# atmosférica debido a esto mismo.
#==============================================================================
ThetaSat=Theta[543:]
LatmosSat=np.abs((400./np.sin(ThetaSat)))
ExtSat=LatmosSat/np.min(LatmosSat)*0.16*0.7#el factor 0.7 es de 70%
ax2=plt.axes()
ax2.plot(ThetaSat,ExtSat,'b',ThetaSat+0.928,ExtSat[::-1],'b',linewidth=2.0)
plt.text(0.5*np.pi/2,0.6,r'$Campo \ de \ vision \ del \ satelite \ desde \ OT$')
plt.twinx()
plt.gca().invert_yaxis()
plt.yticks((np.array([1,2,3,4,5,6,7,8,9,10])*0.1).tolist(),np.array([1,2,3,4,5,6,7,8,9,10]))
plt.ylabel(r'$Masas\ de\ aire$')


print('############################################\n'
'####Angulo#####################Extincion####\n')
print('0 grados               ',Ext[0])
print('90 grados              ',Ext[-1])
print('180 grados             ',Ext[0],)
print('\n############################################')
print('############################################\n'
'#######  Desde el Observatorio del Teide #########\n'
'####Angulo#####################Extincion####\n')

#==============================================================================
# Prueba 3D 
#==============================================================================


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0,2* np.pi, 500)
v = np.linspace(3/2.*np.pi, 2*np.pi, 500)
x = 574.52 * np.outer(np.cos(u), np.sin(v))
y = 574.52 * np.outer(np.sin(u), np.sin(v))
z = 400 * np.outer(np.ones(np.size(u)), np.cos(v))

L=np.sqrt(x**2+y**2+z**2)
Ext=L*0.16/L.max()*10.

# Plot the surface
ax.plot_surface(400/574.52**2*Ext*x, 400/574.52**2*Ext*y, Ext/400*z, cmap=cm.Blues_r,edgecolor='none')
#plt.gca().invert_zaxis()
#ax.set_zticks((np.array(Ext[0][:].tolist())).all(),np.array(Ext[0][::-1].tolist()).all())
plt.title(r'$Extincion\ atmosferica\ \frac{m_{sat}}{m_{sat}+m_{extincion}}\ 3D$')
plt.xlabel(r'$Magnitud\ aparente(m)\ Direccion X$')
plt.ylabel(r'$Magnitud\ aparente(m)\ Direccion Y$')

plt.show()

#==============================================================================
# Boveda celeste que tenemos disponible a la altura de IZAÑA
#==============================================================================

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0,2* np.pi, 500)
v = np.linspace(3/2.*np.pi, 2*np.pi, 500)
x = 174.52 * np.outer(np.cos(u), np.sin(v))
y = 174.52 * np.outer(np.sin(u), np.sin(v))
z = 400 * np.outer(np.ones(np.size(u)), np.cos(v))

L=np.sqrt(x**2+y**2+z**2)
Ext=L*0.16/np.mean(L)

# Plot the surface
ax.plot_surface(x, y, z, cmap=cm.coolwarm,edgecolor='none')


plt.title(r'$Campo\ de\ visio\'n\ desde\ Izana$')
plt.xlabel(r'$Horizonte\ (Km)\ Direccion X$')
plt.ylabel(r'$Horizonte\ (Km)\ Direccion Y$')
ax.set_zlabel(r'$Altura\ hasta\ satelite\ (Km)$')

plt.show()

