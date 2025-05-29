from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import numpy as np

import var
import common as c


def SetupModel(max_iter: int = 1000):
    steps = [
        ("scaler", StandardScaler()),
        (
            "model",
            LogisticRegression(
                max_iter=max_iter,
                class_weight="balanced",
            ),
        ),
    ]
    var.model = Pipeline(steps)
    var.inputs = [
        "rtime_since",
        "vtime_since",
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
