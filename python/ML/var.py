import pandas as pd
from sklearn.base import BaseEstimator

df: pd.DataFrame = None

model: BaseEstimator = None

X_train: pd.DataFrame = None
y_train: pd.DataFrame = None

X_test: pd.DataFrame = None
y_test: pd.DataFrame = None

dummy_input = None
