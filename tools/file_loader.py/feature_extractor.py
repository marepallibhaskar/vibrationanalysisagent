import numpy as np
import pandas as pd
import math

class FeatureExtractor:
    def run(self, clean_signal, fft_result, rpm=None, design_params=None):
        features = {
            "RMS": np.sqrt(np.mean(clean_signal**2)),
            "Kurtosis": pd.Series(clean_signal).kurt(),
            "Skewness": pd.Series(clean_signal).skew(),
            "PeakFreq": fft_result["dominant_freq"]
        }

        # Bearing defect frequency calculations if design parameters are available
        if design_params and rpm:
            n = design_params.get("bearing_balls")
            d = design_params.get("ball_diameter")
            D = design_params.get("pitch_diameter")
            theta = math.radians(design_params.get("contact_angle", 0))
            fr = rpm / 60.0  # convert RPM to Hz

            if n and d and D:
                features["BPFO"] = (n/2.0) * fr * (1 - (d/D) * math.cos(theta))
                features["BPFI"] = (n/2.0) * fr * (1 + (d/D) * math.cos(theta))
                features["BSF"]  = (D/(2.0*d)) * fr * (1 - ((d/D) * math.cos(theta))**2)
                features["FTF"]  = (0.5) * fr * (1 - (d/D) * math.cos(theta))

        return features
