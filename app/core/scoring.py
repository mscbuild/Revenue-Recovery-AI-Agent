def priority_score(risk_value: float, impact: float, confidence: float = 0.9) -> float:
    """
    Weighted priority score combining:
    - risk probability
    - financial impact
    - model confidence
    """
    return risk_value * impact * confidence


def normalize_risk(score: float) -> str:
    if score >= 0.75:
        return "high"
    elif score >= 0.4:
        return "medium"
    return "low"
