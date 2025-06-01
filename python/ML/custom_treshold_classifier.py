from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_X_y, check_array, check_is_fitted


class CustomThresholdClassifier(BaseEstimator, ClassifierMixin):
    def __init__(
        self,
        custom_threshold=0.5,
        max_iter=100,
        class_weight=None,
        solver=None,
        random_state=None,
    ):
        self.custom_threshold = custom_threshold
        self.max_iter = max_iter
        self.class_weight = class_weight
        self.solver = solver
        self.random_state = random_state

        self._estimator_type = "classifier"

    def fit(self, X, y):
        X, y = check_X_y(X, y)
        self.base_model_ = LogisticRegression(
            max_iter=self.max_iter,
            class_weight=self.class_weight,
            solver=self.solver,
            random_state=self.random_state,
        )
        self.base_model_.fit(X, y)
        self.classes_ = self.base_model_.classes_
        return self

    def predict_proba(self, X):
        check_is_fitted(self)
        X = check_array(X)
        return self.base_model_.predict_proba(X)

    def predict(self, X):
        check_is_fitted(self)
        X = check_array(X)
        probabilities = self.base_model_.predict_proba(X)
        prob_positive_class = probabilities[:, 1]
        return (prob_positive_class >= self.custom_threshold).astype(int)
