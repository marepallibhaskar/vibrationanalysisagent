import matplotlib.pyplot as plt
import io
import base64

class Plotter:
    def fft_plot(self, fft_result):
        fig, ax = plt.subplots()
        ax.plot(fft_result["freqs"], fft_result["fft_vals"])
        ax.set_title("FFT Spectrum")
        ax.set_xlabel("Frequency (Hz)")
        ax.set_ylabel("Amplitude")
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")

    def waterfall_plot(self, waterfall_result):
        fig, ax = plt.subplots()
        pcm = ax.pcolormesh(waterfall_result["t"], waterfall_result["f"], 10*np.log10(waterfall_result["Sxx"]))
        fig.colorbar(pcm, ax=ax, label="Power/Frequency (dB/Hz)")
        ax.set_title("Waterfall Plot")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Frequency (Hz)")
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        return base64.b64encode(buf.read()).decode("utf-8")
