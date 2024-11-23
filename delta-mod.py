#delta mod
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the signal
sampling_frequency = 1000
signal_frequency = 5
duration = 1
t = np.linspace(0, duration, int(sampling_frequency * duration), endpoint=False)
analog_signal = np.sin(2 * np.pi * signal_frequency * t)
delta = 0.1  # Step size
dm_signal = np.zeros(len(analog_signal))
encoded_signal = np.zeros(len(analog_signal))

# Initialize the first delta modulation value
dm_signal[0] = 0

# Delta modulation process
for i in range(1, len(analog_signal)):
    # Check if analog signal is higher and adjust delta modulation signal
    if analog_signal[i] > dm_signal[i - 1]:
        dm_signal[i] = dm_signal[i - 1] + delta
        encoded_signal[i] = 1  # Encode as +1 for up
    else:
        # Otherwise, decrease the delta modulation signal
        dm_signal[i] = dm_signal[i - 1] - delta
        encoded_signal[i] = -1  # Encode as -1 for down

# Plot the original and delta-modulated signals
plt.figure(figsize=(12, 6))

# Plot original analog signal
plt.subplot(2, 1, 1)
plt.plot(t, analog_signal, label='Analog Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Analog Signal')
plt.legend()

# Plot delta-modulated signal (using step function for staircase-like behavior)
plt.subplot(2, 1, 2)
plt.step(t, dm_signal, label='Delta-Modulated Signal', color="orange")
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Delta Modulated Signal')
plt.legend()

plt.tight_layout()
plt.show()