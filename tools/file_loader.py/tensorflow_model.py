import tensorflow as tf
import numpy as np

class TensorFlowModel:
    def __init__(self, model_path="models/fault_detection.h5"):
        self.model = tf.keras.models.load_model(model_path)

    def run(self, features):
        arr = np.array([list(features.values())])
        pred = self.model.predict(arr)
        fault_idx = np.argmax(pred)
        confidence = pred[0][fault_idx]
        fault_types = ["Cavitation","Turbulence","Misalignment",
                       "Looseness","Bearing Fault","Gear Fault"]
        return {"fault": fault_types[fault_idx], "confidence": confidence}
