import numpy as np
from scipy.signal import detrend

class SignalPreprocessor:
    def run(self, raw_signal):
        signal = detrend(raw_signal)
        signal = signal - np.mean(signal)
        signal = signal / np.max(np.abs(signal))
        return signal
