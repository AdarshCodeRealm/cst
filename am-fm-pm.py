#am fm pm 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# Define parameters
fm = 5  # Message frequency (Hz)
fc = 50  # Carrier frequency (Hz)
fs = 1000  # Sampling frequency (Hz)
t = np.arange(0, 1, 1 / fs)  # Time axis

# Define message and carrier signals
message_signal = np.sin(2 * np.pi * fm * t)
carrier_signal = np.sin(2 * np.pi * fc * t)

# Define modulation parameters
m = 0.5  # Modulation index for AM
kp = 2  # Phase constant for PM
kf = 5  # Frequency sensitivity for FM

# Define AM, FM, PM signals
am_signal = (1 + m * message_signal) * carrier_signal  # Amplitude Modulation
fm_signal = np.cos(2 * np.pi * fc * t + kp * np.cumsum(message_signal))  # Frequency Modulation
pm_signal = np.cos(2 * np.pi * fc * t + kf * message_signal)  # Phase Modulation

# Create a subplot grid
plt.figure(figsize=(15, 8))
gs = gridspec.GridSpec(3, 2, height_ratios=[1, 1, 0.5])

# Plot message and carrier signals
plt.subplot(gs[0, 0])
plt.plot(t, message_signal, color='b')
plt.title('Message Signal')
plt.subplot(gs[0, 1])
plt.plot(t, carrier_signal, color='g')
plt.title('Carrier Signal')

# Plot AM, FM, PM signals
plt.subplot(gs[1, 0])
plt.plot(t, am_signal, color='r')
plt.title('Amplitude Modulated Signal')
plt.subplot(gs[1, 1])
plt.plot(t, fm_signal, color='y')
plt.title('Frequency Modulated Signal')
plt.subplot(gs[2, :])
plt.plot(t, pm_signal, color='c')
plt.title('Phase Modulated Signal')

# Adjust layout
plt.tight_layout()
plt.show()