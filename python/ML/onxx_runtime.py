import onnxruntime as ort
import numpy as np


class SklearnONNXPredictor:
    def __init__(self, model_path):
        self.session = ort.InferenceSession(model_path)
        self.input_name = self.session.get_inputs()[0].name

    def predict(self, X):
        if hasattr(X, "to_numpy"):
            X = X.to_numpy()
        X = X.astype(np.int64)
        outputs = self.session.run(None, {self.input_name: X})
        return outputs[0]
