from sklearn.linear_model import LogisticRegression
import numpy as np

import var
import common as c


def SetupModel(max_iter: int = 1000):
    var.model = LogisticRegression(
        max_iter=max_iter, class_weight="balanced", n_jobs=-1
    )
    var.cols = [
        "rtime_since_log",
        "clock_freq_log",
        "wasted",
    ]
    var.input_dtype = np.float32


def SetupData():
    c.SetupData()


Train = c.Train

# Hardly Need Modification
Test = c.Test
AddDatasets = c.AddDatasets
DescribeData = c.DescribeData
ExportONNX = c.ExportONNX
LoadONNX = c.LoadONNX
SaveModel = c.SaveModel
LoadModel = c.LoadModel
PlotSave = c.PlotSave
PlotShow = c.PlotShow
