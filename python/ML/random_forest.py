from sklearn.ensemble import RandomForestClassifier

import var


def SetupModel(max_iter: int = 100):
    if var.df is None:
        raise Exception("Datasets has not been set up")
    var.model = RandomForestClassifier(
        n_jobs=-1,
        n_estimators=100,
        max_depth=None,
        max_features="sqrt",
        bootstrap=True,
        random_state=9,
    )


def Train():
    if var.df is None:
        raise Exception("Datasets has not been set up")
    if var.model is None:
        raise Exception("Model has not been set up")
    var.model.fit(var.X_train, var.y_train)
