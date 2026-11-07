
from pydantic import BaseModel, Field


class ForecastRequest(BaseModel):
    series: list[float] = Field(
        ...,
        min_length=12,
        description="Historical economic observations"
    )

    horizon: int = Field(
        default=4,
        ge=1,
        le=40
    )

    variable_name: str = "inflation"


class ForecastResponse(BaseModel):
    variable_name: str
    horizon: int
    predictions: list[float]
    model_name: str
    status: str
    research_note: str
