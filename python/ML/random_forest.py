from sklearn.ensemble import RandomForestClassifier

import var


def SetupModel(max_depth: int = 20, n_estimators: int = 100, parallelism: int = 4):
    if var.df is None:
        raise Exception("Datasets has not been set up")
    var.model = RandomForestClassifier(
        n_jobs=parallelism,
        n_estimators=n_estimators,
        max_depth=max_depth,
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
