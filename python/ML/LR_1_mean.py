from sklearn.linear_model import LogisticRegression
import numpy as np

import var
import common as c


def SetupModel(max_iter: int = 1000):
    var.model = LogisticRegression(
        max_iter=max_iter, class_weight="balanced", n_jobs=-1
    )
    var.inputs = [
        "rtime_since_log",
        "vtime_since_log",
        "clock_freq_std",
        "lifetime_freq_std",
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
AddDatasets = c.AddDatasets
DescribeData = c.DescribeData
ExportONNX = c.ExportONNX
LoadONNX = c.LoadONNX
SaveModel = c.SaveModel
LoadModel = c.LoadModel
PlotSave = c.PlotSave
PlotShow = c.PlotShow
