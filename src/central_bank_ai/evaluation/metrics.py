
import numpy as np

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error
)


def calculate_metrics(
    actual,
    predicted
):

    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)

    if actual.shape != predicted.shape:
        raise ValueError(
            "Actual and predicted shapes must match"
        )

    if actual.size == 0:
        raise ValueError(
            "Evaluation data cannot be empty"
        )

    if not (
        np.isfinite(actual).all()
        and np.isfinite(predicted).all()
    ):
        raise ValueError(
            "Evaluation data must be finite"
        )

    mae = mean_absolute_error(
        actual,
        predicted
    )

    rmse = np.sqrt(
        mean_squared_error(actual, predicted)
    )

    return {
        "MAE": float(mae),
        "RMSE": float(rmse)
    }
