
from central_bank_ai.evaluation.metrics import (
    calculate_metrics
)


def test_metrics():

    result = calculate_metrics(
        [10, 20, 30],
        [11, 19, 30]
    )

    assert result["MAE"] > 0

    assert result["RMSE"] > 0


def test_perfect_prediction():

    result = calculate_metrics(
        [10, 20, 30],
        [10, 20, 30]
    )

    assert result["MAE"] == 0

    assert result["RMSE"] == 0
