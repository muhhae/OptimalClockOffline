from sklearn.linear_model import LogisticRegression

import var
import common as c


def SetupModel(max_iter: int = 1000):
    if var.df is None:
        raise Exception("Datasets has not been set up")
    var.model = LogisticRegression(max_iter=max_iter)


def SetupData():
    if var.df is None:
        raise Exception("Datasets has not been loaded, exec AddDatasets")
    var.df["obj_size_percent"] = var.df["obj_size"] / var.df["cache_size"] * 1e6
    var.df.drop(["obj_size", "cache_size"], axis=1, inplace=True)
    c.SetupData()


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
