#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PHS2061 Lab - Charge to Mass Ratio of Electron
# Guy Faiman, Oscar Lemonidis, Josh Clark

import numpy as np
import matplotlib.pyplot as plt
import monashspa.PHS2061 as spa
import sympy as sp

print("-----------------------------DATA ENTRY------------------------------")
# Voltage , Current , Radius measurements
dataList = [
    [150 , 1.663 , 3.35 ],
    [160 , 1.663 , 3.58 ],
    [170 , 1.663 , 3.7  ],
    [180 , 1.663 , 3.8  ],
    [190 , 1.663 , 3.95 ],
    [200 , 1.663 , 4.05 ],
    [210 , 1.663 , 4.3  ],
    [220 , 1.663 , 4.55 ],
    [230 , 1.663 , 4.6  ],
    [240 , 1.663 , 4.75 ],
    [250 , 1.663 , 4.85 ]
    ]
     
     
dataA = np.array(dataList)
V = dataA[:,0]
B = dataA[:,1]*7.8*(10**-4)
R = dataA[:,2]/100
u_V = 0.005
u_R = 0.005
u_B = 0.0005*10**-4

print("-----------------------Symbolic data-------------------------")
# symbolic variable only for T as it changes after logging it
sV = sp.Symbol('V')
u_sV = sp.Symbol('u_V')
sR = sp.Symbol('R')
u_sR = sp.Symbol('u_R')
sB = sp.Symbol('B')
u_sB = sp.Symbol('u_B')
symbols = np.array([sB,sR])
u_symbols = np.array([u_sB,u_sR])
expr_y = (sB**2)*(sR**2)/2

derivs = np.array(expr_y.diff(symbols))
derivs = derivs*u_symbols
derivs = np.dot(derivs,derivs)
derivs = sp.sqrt(derivs)
print(sp.pretty(derivs))


y_data = (B**2)*(R**2)/2
u_expr_y_f = sp.lambdify([sB,u_sB,sR,u_sR],derivs)
u_expr = u_expr_y_f(B,u_B,R,u_R)

x_data = V

print("--------------------Linearising the data-------------------")
#Linear fitting
linear_data=np.transpose([x_data,0,y_data,u_expr])
# perform the fit
fit_results=spa.linear_fit(x_data,y_data,u_y=u_expr)
# get the fit points and 1 sigma uncertainties
y_fit=fit_results.best_fit
u_y_fit=fit_results.eval_uncertainty(sigma=1)
# extract the fit parameters

fit_parameters=spa.get_fit_parameters(fit_results)

plt.figure(3)
plt.title("Linearised data for electron charge mass ratio")
plt.errorbar(x_data, y_data, xerr=0, yerr=u_expr, marker="o", linestyle="None",label="Data points")
plt.plot(x_data,y_fit,marker="None",linestyle="-",color="black",label="Line of Best Fit")
plt.fill_between(x_data,y_fit-u_y_fit,y_fit+u_y_fit,color="lightgrey",label="1-$\sigma$ Spread in Fit")
plt.legend(bbox_to_anchor=(1,1))
plt.xlabel("V")
plt.ylabel("B**2R**2/2")
spa.savefig('Lab2_chargemassratio.png')
plt.show()

#gradient

gradient=fit_parameters["slope"]
chargemass = 1/gradient
print("e/m: {:e}".format(chargemass))