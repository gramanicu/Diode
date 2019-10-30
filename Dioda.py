import matplotlib.pyplot as plt
import numpy as np

# Specific Values
I0 = 10**-9
n = 2
vstart = 0.01
vstop = 0.9
vstep = 0.01

Vd = np.arange(vstart, vstop, vstep)  # The array of Voltages

def shockley(I0, n, T, Vd):
    q = 1.602176 * (10**-19)
    k = 1.380649 * (10**-23)
    I = I0 * ( np.exp((q * Vd) / (n * k * T)) - 1)     # The Shockley equation
    return I


temps = np.arange(250, 300, 10)

for T in temps:
    plt.plot(Vd, shockley(I0, n, T, Vd), label = "Current at {}K".format(T))

axes = plt.gca()
axes.set_xticks(np.arange(vstart, vstop, vstep*10))
axes.set_yticks(np.arange(0, 1, 0.05))
plt.xlabel("Voltage V")
plt.ylabel("Current A")
plt.title("Diode characteristics")
plt.legend()
plt.grid()
plt.savefig("Graph.png")