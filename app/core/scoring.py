def priority_score(risk_value, confidence=0.9):
    """
    Combines financial impact + confidence into a single score.
    """
    return risk_value * confidence


def normalize_risk(score: float) -> str:
    if score >= 0.75:
        return "high"
    elif score >= 0.4:
        return "medium"
    return "low"
