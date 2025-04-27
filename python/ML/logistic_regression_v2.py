from sklearn.linear_model import LogisticRegression
import numpy as np

import var
import common as c


def SetupModel(max_iter: int = 1000):
    if var.df is None:
        raise Exception("Datasets has not been set up")
    var.model = LogisticRegression(max_iter=max_iter)


def SetupData():
    c.SetupData()
    time_begin = (
        var.X_train["clock_time"].min()
        if var.X_train["clock_time"].min() < var.X_test["clock_time"].min()
        else var.X_test["clock_time"].min()
    )
    for x in [var.X_train, var.X_test]:
        x["time_since"] = x["clock_time"] - time_begin
        x["obj_size_relative"] = (x["obj_size"] / x["cache_size"] * 1e6).astype(
            np.int64
        )
        x.drop(["obj_size", "cache_size", "clock_time"], axis=1, inplace=True)


Train = c.Train

# Hardly Need Modification
Test = c.Test
AddDatasets = c.AddDatasets
DescribeData = c.DescribeData
ExportONNX = c.ExportONNX
SaveModel = c.SaveModel
LoadModel = c.LoadModel
PlotSave = c.PlotSave
PlotShow = c.PlotShow
