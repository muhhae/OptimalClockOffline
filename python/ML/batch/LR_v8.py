from sklearn.linear_model import LogisticRegression

import var
import common as c


def SetupModel(max_iter: int = 1000):
    var.model = LogisticRegression(
        max_iter=max_iter, class_weight="balanced", n_jobs=-1
    )
    var.cols = [
        "clock_time_between",
        "clock_freq",
        "lifetime_freq",
        "wasted",
    ]


def SetupData():
    cols = [
        "clock_time_between",
        "clock_freq",
        "lifetime_freq",
    ]
    c.SetupData()
    for x in [var.X_train, var.X_test]:
        for col in cols:
            x[f"{col}_normalized"] = x[col] / x[col].max()


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
