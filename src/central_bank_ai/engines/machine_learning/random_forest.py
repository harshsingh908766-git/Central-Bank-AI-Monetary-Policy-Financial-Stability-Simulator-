
import numpy as np

from sklearn.ensemble import RandomForestRegressor


class EconomicRandomForest:

    def __init__(self, random_state=42):

        self.model = RandomForestRegressor(
            n_estimators=300,
            max_depth=8,
            min_samples_leaf=2,
            random_state=random_state,
            n_jobs=-1
        )

    def train(self, X, y):

        X = np.asarray(X, dtype=float)
        y = np.asarray(y, dtype=float)

        if X.ndim != 2 or y.ndim != 1:
            raise ValueError(
                "Expected 2D features and 1D target"
            )

        if len(X) != len(y) or len(y) < 10:
            raise ValueError(
                "Insufficient or mismatched training data"
            )

        if not (
            np.isfinite(X).all()
            and np.isfinite(y).all()
        ):
            raise ValueError(
                "Training data contains non-finite values"
            )

        self.model.fit(X, y)

        return self

    def predict(self, X):

        return self.model.predict(X).tolist()
