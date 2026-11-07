
from fastapi import APIRouter, HTTPException

from central_bank_ai.api.schemas import (
    ForecastRequest,
    ForecastResponse
)

from central_bank_ai.services.forecast_service import (
    generate_forecast
)

router = APIRouter(prefix="/api/v1", tags=["Central Bank AI"])


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "project": "Central Bank AI",
        "version": "0.1.0"
    }


@router.post(
    "/forecast",
    response_model=ForecastResponse
)
def forecast(
    request: ForecastRequest
):

    try:
        return generate_forecast(request)

    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail=str(error)
        ) from error
