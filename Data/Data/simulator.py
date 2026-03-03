import numpy as np
import pandas as pd

# Parameters
fs = 20000  # sampling frequency (Hz)
duration = 1.0  # seconds
N = int(fs * duration)  # 20,000 samples

# Time vector
t = np.arange(N) / fs

# Synthetic vibration signal: mix of sine + noise + defect impulses
signal = 0.02*np.sin(2*np.pi*250*t) + 0.01*np.sin(2*np.pi*500*t)
signal += 0.005*np.random.randn(N)

# Add defect impulses every 0.05s
for i in range(0, N, int(0.05*fs)):
    signal[i:i+5] += 0.05

# Save to CSV
df = pd.DataFrame({"time": t, "acceleration": signal})
df.to_csv("sample_bearing_20k.csv", index=False)
print("Saved sample_bearing_20k.csv with 20,000 rows")
