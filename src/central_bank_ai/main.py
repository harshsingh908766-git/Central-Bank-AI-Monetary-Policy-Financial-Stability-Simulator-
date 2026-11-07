
from fastapi import FastAPI

from central_bank_ai.api.routes import router


app = FastAPI(
    title="Central Bank AI",
    description=(
        "AI-driven macro-financial intelligence "
        "and monetary policy research platform."
    ),
    version="0.1.0"
)

app.include_router(router)


@app.get("/")
def root():

    return {
        "project": "Central Bank AI",
        "message": "Research platform is running",
        "api_documentation": "/docs",
        "disclaimer": (
            "Research decision-support prototype. "
            "Not an autonomous policy system."
        )
    }
