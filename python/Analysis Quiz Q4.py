#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# PHS2061 - Analysis Quiz Q4
# Josh Clark, 4th March 2023

import numpy as np
import matplotlib.pyplot as plt
import monashspa.PHS2061 as spa

data = np.array([
        #length change [m], u in length change)[mm], temperature, [degree C]
        [0.018252,  0.002000,    -20],
        [0.018365,  0.002000,    -10],
        [0.018947,  0.002000,      0],
        [0.023589,  0.002000,     10],
        [0.021967,  0.002000,     20],
        [0.028465,  0.002000,     30],
        [0.029391,  0.002000,     40],
    ])

# GP: NOTE CAN SCALE INTO 10^(-3) m
x_data = data[:,2]
y_data = data[:,0]
u_y_data = data[:,1]

plt.figure(1)
plt.title("Thermal expansion")
# GP: added label = "thermal expansion"

plt.axvline(x=0,color='gray',linewidth=1, linestyle=':')
plt.errorbar(x_data, y_data, yerr=u_y_data, marker="o", linestyle= "None")
plt.xlabel("Temperature [degrees Celcius]")
plt.ylabel ("Length change [m]")
plt.xlim([-25,45])

# GP: CHANGE YLIM
# OLD plt.ylim([0,36])
# NEW
plt.ylim([0.0145,0.0325])

#spa.savefig('figure1.png')
plt.show()

fit_results = spa.linear_fit(x_data, y_data, u_y= u_y_data)
y_fit = fit_results.best_fit

# GP: SIGMA NOT SIGMNA
u_y_fit = fit_results.eval_uncertainty(sigma=2)

plt.figure(2)
plt.axvline(x=0,color='gray',linewidth=1, linestyle='--')
plt.title("Figure 2:Thermal expansion")
plt.errorbar(x_data, y_data, yerr=u_y_data, marker="o", linestyle= "None", color = 'black', label = "thermal expansion")
plt.plot(x_data, y_fit, marker = 'None', linestyle = "-", color = "black", label = "linear fit")
plt.fill_between(x_data, y_fit-u_y_fit, y_fit+u_y_fit, color = "lightgrey", label = "uncertainity in linear fit")
plt.xlabel("Temperature [degrees Celcius]")
plt.ylabel("Length change [m]")

# GP: CHANGE XLIM AND YLIM
# OLD
#plt.xlim([0,50])
#plt.ylim([0,0.036])
# NEW
plt.xlim([-25,45])
plt.ylim([0.0145,0.0325])

plt.legend(bbox_to_anchor=(1,1))
#spa.savefig('figure2.png')
plt.show()


fit_parameters = spa.get_fit_parameters(fit_results)
print (fit_parameters)

gradient = fit_parameters ["slope"]
u_gradient = fit_parameters["u_slope"]