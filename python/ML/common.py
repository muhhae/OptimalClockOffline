from skl2onnx import to_onnx
from skl2onnx.common.data_types import (
    FloatTensorType,
    Int64TensorType,
    StringTensorType,
    BoolTensorType,
)
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from typing import List, Tuple, Union

import var
import logistic_regression as lr

DataType = Union[FloatTensorType, Int64TensorType, StringTensorType, BoolTensorType]


def DescribeData():
    if var.df is None:
        raise Exception("Datasets has not been loaded, exec AddDatasets")
    print("\n🧾 Basic Info:")

    print("-" * 60)
    print(var.df.info())

    print("\n📊 Summary Statistics (Numerical Columns):")
    print("-" * 60)
    print(var.df.describe(include=[float, int]))

    print("\n📌 Missing Values:")
    print("-" * 60)
    print(var.df.isnull().sum())

    print("\n🆔 Unique Values per Column:")
    print("-" * 60)
    print(var.df.nunique())

    if "wasted" in var.df.columns:
        print("\n🚫 Subset: wasted == 0")
        print("-" * 60)
        print(var.df[var.df["wasted"] == 0].describe(include=[float, int]))

        print("\n✅ Subset: wasted == 1")
        print("-" * 60)
        print(var.df[var.df["wasted"] == 1].describe(include=[float, int]))
    else:
        print("\n⚠️ Column 'wasted' not found in CSV.")


def AddDatasets(*paths: str):
    new_df = pd.concat([pd.read_csv(p) for p in paths], ignore_index=True)
    new_df.columns = new_df.columns.str.strip()
    new_df = new_df.drop(
        [
            "last_access_rtime",
            "last_access_vtime",
            "create_rtime",
            "compulsory_miss",
            "first_seen",
        ],
        axis=1,
    )
    if var.df is None:
        var.df = new_df
    else:
        var.df = pd.concat([var.df, new_df], ignore_index=True)


def SetupData():
    if var.df is None:
        raise Exception("Datasets has not been loaded, exec AddDatasets")
    X = var.df.iloc[:, :-1]
    y = var.df.wasted
    var.X_train, var.X_test, var.y_train, var.y_test = train_test_split(
        X, y, test_size=0.2, random_state=9, stratify=y
    )
    var.dummy_input = var.X_train[:1]


def LoadModel(path: str = "model.pkl"):
    var.model = joblib.load(path)


def SaveModel(path: str = "model.pkl"):
    if var.model is None:
        raise Exception("Model has not been set up, exec SetupModel and Train")
    joblib.dump(var.model, path)


def ExportONNX(
    path: str = "model.onxx",
):
    if var.model is None:
        raise Exception("Model has not been set up, exec SetupModel and Train")
    if var.dummy_input is None:
        raise Exception("Provide var.dummy_input or SetupData()")
    onx = to_onnx(var.model, var.dummy_input)
    file = open(path, "wb")
    file.write(onx.SerializeToString())
    file.close()


def Test():
    if var.X_test is None:
        raise Exception("Datasets has not been set up, exec SetupData")
    if var.model is None:
        raise Exception("Model has not been set up, exec SetupModel and Train")
    predictions = var.model.predict(var.X_test)
    print("Classification Report:")
    print(classification_report(var.y_test, predictions))
    print("Accuracy:", accuracy_score(var.y_test, predictions))
    cm = confusion_matrix(var.y_test, predictions)
    print("Confusion Matrix:")
    print(cm)
    print("Confusion Matrix (%):")
    print(cm / cm.sum() * 100)


def PlotSave(path: str = "plot.png"):
    if var.model is None:
        raise Exception("Model has not been set up, exec SetupModel and Train")
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        confusion_matrix(var.y_test, var.model.predict(var.X_test)),
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Not Wasted (0)", "Wasted (1)"],
        yticklabels=["Not Wasted (0)", "Wasted (1)"],
    )
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.savefig(path)


def PlotShow():
    if var.model is None:
        raise Exception("Model has not been set up, exec SetupModel and Train")
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        confusion_matrix(var.y_test, var.model.predict(var.X_test)),
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Not Wasted (0)", "Wasted (1)"],
        yticklabels=["Not Wasted (0)", "Wasted (1)"],
    )
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.show()
