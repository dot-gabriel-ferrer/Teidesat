# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:33:09 2018

@author: Gabriel
"""

import numpy as np

h1,h2,h3,h4,h5,h6,h7=np.arange(0,11.1,0.1), np.arange(11,20.1,0.1),np.arange(20,32.1,0.1),np.arange(32,47.1,0.1),np.arange(47,51.1,0.1),np.arange(51,71.1,0.1),np.arange(71,84.854,0.1)
h8,h9,h10,h11,h12=np.arange(86,91.1,0.1),np.arange(91,100.1,0.1),np.arange(100,110.1,0.1),np.arange(110,120.1,0.1),np.arange(120,150.1,0.1)
h13,h14,h15=np.arange(150,200.1,0.1),np.arange(200,300.1,0.1),np.arange(300,500.1,0.1)
L=np.array([h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15])
def H():

    h=[]
    for i in range(0,15):
        h.append(L[i])
    
    h=np.array(h)
    return h