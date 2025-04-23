from sklearn.linear_model import LogisticRegression

import var


def SetupModel(max_iter: int = 100):
    if var.df is None:
        raise Exception("Datasets has not been set up")
    var.model = LogisticRegression(max_iter=max_iter)


def Train():
    if var.df is None:
        raise Exception("Datasets has not been set up")
    if var.model is None:
        raise Exception("Model has not been set up")
    var.model.fit(var.X_train, var.y_train)
