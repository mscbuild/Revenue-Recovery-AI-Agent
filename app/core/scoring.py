def priority_score(risk_value, confidence=0.9):
    """
    Combines financial impact + confidence into a single score.
    """
    return risk_value * confidence
