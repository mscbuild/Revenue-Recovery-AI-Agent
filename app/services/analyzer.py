from app.core.rules import stalled_deal_risk, overdue_invoice_risk
from app.core.scoring import priority_score
from app.config import settings
from app.services.logger import logger


class AnalyzerService:
    """
    Transforms raw business data into structured risk alerts.
    """

    def analyze_deals(self, deals):
        alerts = []

        for deal in deals:
            risk = stalled_deal_risk(deal)

            if risk > 0:
                score = priority_score(risk, settings.default_confidence)

                alert = {
                    "type": "stalled_deal",
                    "customer": deal.customer,
                    "risk_value": risk,
                    "priority_score": score,
                    "confidence": settings.default_confidence,
                    "action": f"Contact {deal.customer} immediately",
                }

                alerts.append(alert)

                logger.info(f"Stalled deal detected: {deal.customer} | Risk={risk}")

        return alerts

    def analyze_invoices(self, invoices):
        alerts = []

        for inv in invoices:
            risk = overdue_invoice_risk(inv)

            if risk > 0:
                score = priority_score(risk, 0.95)

                alert = {
                    "type": "overdue_invoice",
                    "customer": inv.customer,
                    "risk_value": risk,
                    "priority_score": score,
                    "confidence": 0.95,
                    "action": f"Send payment reminder to {inv.customer}",
                }

                alerts.append(alert)

                logger.info(f"Overdue invoice detected: {inv.customer} | Risk={risk}")

        return alerts
