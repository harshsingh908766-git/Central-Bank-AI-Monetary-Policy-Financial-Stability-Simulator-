
from central_bank_ai.api.schemas import (
    ForecastRequest,
    ForecastResponse
)


def generate_forecast(
    request: ForecastRequest
) -> ForecastResponse:

    values = request.series

    if not values:
        raise ValueError("Input series cannot be empty")

    if not all(
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        for value in values
    ):
        raise ValueError("Series must contain numeric values")

    last_value = float(values[-1])

    predictions = [
        last_value for _ in range(request.horizon)
    ]

    return ForecastResponse(
        variable_name=request.variable_name,
        horizon=request.horizon,
        predictions=predictions,
        model_name="Naive Persistence Baseline",
        status="experimental",
        research_note=(
            "Baseline forecast only. "
            "Not a validated monetary policy forecast."
        )
    )
