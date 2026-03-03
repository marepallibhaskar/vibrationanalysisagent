from scipy.signal import spectrogram

class WaterfallTool:
    def run(self, clean_signal, fs=10000, window=1024):
        f, t, Sxx = spectrogram(clean_signal, fs, nperseg=window)
        return {"f": f, "t": t, "Sxx": Sxx}
