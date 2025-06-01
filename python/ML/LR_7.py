from custom_treshold_classifier import CustomThresholdClassifier
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
import numpy as np

import var
import common as c


def SetupModel(max_iter: int = 1000):
    steps = [
        ("scaler", RobustScaler()),
        (
            "model",
            CustomThresholdClassifier(
                custom_threshold=0.3,
                max_iter=max_iter,
                class_weight="balanced",
                solver="liblinear",
                random_state=42,
            ),
        ),
    ]
    var.model = Pipeline(steps)
    var.inputs = [
        "rtime_since_log",
        "vtime_since_log",
        "clock_freq",
        "lifetime_freq",
    ]
    var.input_dtype = np.float32


Train = c.Train

# Hardly Need Modification
AddDatasets = c.AddDatasets
ResetDatasets = c.ResetDatasets
LoadDatasets = c.LoadDatasets
SetTestData = c.SetTestData
SetTrainData = c.SetTrainData
SplitData = c.SplitData
Test = c.Test
DescribeData = c.DescribeData
ExportONNX = c.ExportONNX
LoadONNX = c.LoadONNX
SaveModel = c.SaveModel
LoadModel = c.LoadModel
PlotSave = c.PlotSave
PlotShow = c.PlotShow
