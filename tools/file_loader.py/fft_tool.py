import numpy as np
from scipy.fftpack import fft

class FFTTool:
    def run(self, clean_signal, fs=10000):
        N = len(clean_signal)
        freqs = np.fft.fftfreq(N, 1/fs)
        fft_vals = np.abs(fft(clean_signal))[:N//2]
        dominant_freq = freqs[np.argmax(fft_vals)]
        return {"freqs": freqs[:N//2], "fft_vals": fft_vals, "dominant_freq": dominant_freq}
