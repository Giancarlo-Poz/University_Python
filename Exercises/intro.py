#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:37:59 2022

@author: giancarlo
"""

import numpy as np
import matplotlib.pyplot as plt
import monashspa.PHS2061 as spa

a = [1,2,3,4]
print(a)
print(2*a)

a = np.array(a)
print(2*a)

c = [
     [ 1, 2, 3, 4],
     [ 5, 6, 7, 8],
     [ 9,10,11,12],
     [13,14,15,16]]

c = np.array(c)

print(c[1,2])
print(c[1,:])