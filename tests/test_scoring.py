from app.core.scoring import priority_score

def test_priority_score():
    assert priority_score(1000, 1.0) == 1000
    assert priority_score(1000, 0.5) == 500
