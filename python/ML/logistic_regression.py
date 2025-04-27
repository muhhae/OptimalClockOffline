from sklearn.linear_model import LogisticRegression

import var
import common as c


def SetupModel(max_iter: int = 100):
    if var.df is None:
        raise Exception("Datasets has not been set up")
    var.model = LogisticRegression(max_iter=max_iter)


Train = c.Train
Test = c.Test
AddDatasets = c.AddDatasets
DescribeData = c.DescribeData
ExportONNX = c.ExportONNX
SaveModel = c.SaveModel
LoadModel = c.LoadModel
PlotSave = c.PlotSave
PlotShow = c.PlotShow
SetupData = c.SetupData
