# Copyright 2019 Grama Nicolae

import matplotlib.pyplot as plt
import numpy as np

# Specific Values
I0 = 10**-9
n = 2

# Voltage range
vstart = 0.01
vstop = 0.9
vstep = 0.01

Vd = np.arange(vstart, vstop, vstep)  # Creates the voltages array

# A function to compute the result of the Shockley Formula
def shockley(I0, n, T, Vd):
    q = 1.602176 * (10**-19)    # The elementary charge of the electron
    k = 1.380649 * (10**-23)    # Boltzmann's Constant

    I = I0 * ( np.exp((q * Vd) / (n * k * T)) - 1)  # The formula
    return I

''' We will plot the currents for a range of temperatures
    250, 260, 270, 280, 290, 300 K (Kelvin)
'''
temps = np.arange(250, 300, 10)

# Plot the result for each temperature
for T in temps:
    plt.plot(Vd, shockley(I0, n, T, Vd), label = "Current at {}K".format(T))

# Plot styling
axes = plt.gca()
axes.set_xticks(np.arange(vstart, vstop, vstep*10))
axes.set_yticks(np.arange(0, 1, 0.05))
plt.xlabel("Voltage V")
plt.ylabel("Current A")
plt.title("Diode characteristics")
plt.legend()
plt.grid()
plt.savefig("./images/Diode.png")