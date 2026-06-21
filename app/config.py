from dataclasses import dataclass

@dataclass
class Settings:
    """
    Global configuration for Revenue Recovery Agent.
    """

    # Risk thresholds
    deal_stale_days: int = 14
    invoice_overdue_days: int = 30

    # Risk multipliers
    stalled_deal_risk_multiplier: float = 0.30

    # Scoring
    default_confidence: float = 0.9

    # Output
    currency_symbol: str = "$"


settings = Settings()
