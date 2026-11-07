
def calculate_composite_risk(
    credit_risk,
    liquidity_risk,
    market_risk,
    network_risk
):

    components = [
        credit_risk,
        liquidity_risk,
        market_risk,
        network_risk
    ]

    if any(
        not 0 <= value <= 100
        for value in components
    ):
        raise ValueError(
            "Risk components must be between 0 and 100"
        )

    weights = {
        "credit": 0.30,
        "liquidity": 0.25,
        "market": 0.25,
        "network": 0.20
    }

    score = (
        credit_risk * weights["credit"]
        + liquidity_risk * weights["liquidity"]
        + market_risk * weights["market"]
        + network_risk * weights["network"]
    )

    return {
        "composite_risk_score": round(score, 2),
        "status": "experimental",
        "methodology": "Illustrative weighted indicator"
    }
