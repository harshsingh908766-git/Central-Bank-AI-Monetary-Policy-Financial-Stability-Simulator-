
from fastapi.testclient import TestClient

from central_bank_ai.main import app

client = TestClient(app)


def test_health():

    response = client.get("/api/v1/health")

    assert response.status_code == 200

    assert response.json()["status"] == "healthy"


def test_forecast():

    response = client.post(
        "/api/v1/forecast",
        json={
            "series": [
                2.1, 2.2, 2.3, 2.4,
                2.5, 2.6, 2.7, 2.8,
                2.9, 3.0, 3.1, 3.2
            ],
            "horizon": 4,
            "variable_name": "inflation"
        }
    )

    assert response.status_code == 200

    result = response.json()

    assert len(result["predictions"]) == 4

    assert result["model_name"] == (
        "Naive Persistence Baseline"
    )


def test_insufficient_observations():

    response = client.post(
        "/api/v1/forecast",
        json={
            "series": [1.0, 2.0],
            "horizon": 4
        }
    )

    assert response.status_code == 422
