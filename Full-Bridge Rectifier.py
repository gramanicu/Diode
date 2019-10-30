# Copyright 2019 Grama Nicolae

import math as math
import matplotlib.pyplot as plt
import numpy as np

A = 12  # Amplitude
f = 50  # Frequency
Vo = 0.6 # Threshold Voltage for the diode

t = 0.1        # Time interval (max, in seconds)
samples = 2000 # Number of samples

time = np.linspace(0, t, samples);

V = A * np.sin((2 * f * math.pi) * time);   # Input signal

# Input signal plot
plt.subplot(2, 1, 1)
plt.plot(time, V)
plt.ylabel("Input Voltage (Volts)")
plt.title("Full-Bridge Rectifier")
axes = plt.gca()
axes.set_xticks(np.arange(0, 0.11, 0.01))
axes.set_yticks(np.arange(-15, 15, 3))
plt.grid()

# Output signal plot                                        
plt.subplot(2, 1, 2)
plt.plot(time, np.abs(V) - 2 * Vo)
plt.ylabel("Output Voltage (Volts)")
plt.xlabel("Time (seconds)")
axes = plt.gca()
axes.set_xticks(np.arange(0, 0.11, 0.01))
axes.set_yticks(np.arange(0, 15, 3.6))
plt.grid()
plt.savefig("./images/Full-Bridge_Rectifier.png")

