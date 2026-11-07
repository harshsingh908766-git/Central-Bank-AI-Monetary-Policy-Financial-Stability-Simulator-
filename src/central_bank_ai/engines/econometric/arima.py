
import numpy as np
from statsmodels.tsa.arima.model import ARIMA


def train_arima(
    observations: list[float],
    horizon: int = 4,
    order: tuple = (1, 1, 1)
):

    if len(observations) < 12:
        raise ValueError(
            "At least 12 observations are required"
        )

    if horizon < 1:
        raise ValueError(
            "Horizon must be positive"
        )

    values = np.asarray(
        observations,
        dtype=float
    )

    if not np.isfinite(values).all():
        raise ValueError(
            "Observations must be finite"
        )

    model = ARIMA(
        values,
        order=order
    )

    fitted_model = model.fit()

    forecast_result = fitted_model.get_forecast(
        steps=horizon
    )

    predictions = forecast_result.predicted_mean

    confidence_interval = (
        forecast_result.conf_int()
    )

    return {
        "model": "ARIMA",
        "predictions": predictions.tolist(),
        "confidence_interval": (
            confidence_interval.tolist()
        ),
        "status": "experimental"
    }
