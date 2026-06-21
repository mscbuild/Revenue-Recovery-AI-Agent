from app.core.rules import stalled_deal_risk, overdue_invoice_risk

class RevenueRecoveryAgent:
    def __init__(self):
        self.alerts = []

    def analyze_deals(self, deals):
        for deal in deals:
            risk = stalled_deal_risk(deal)

            if risk > 0:
                self.alerts.append({
                    "type": "stalled_deal",
                    "customer": deal.customer,
                    "risk_value": risk,
                    "confidence": 0.85,
                    "action": f"Contact {deal.customer} within 24 hours"
                })

    def analyze_invoices(self, invoices):
        for inv in invoices:
            risk = overdue_invoice_risk(inv)

            if risk > 0:
                self.alerts.append({
                    "type": "overdue_invoice",
                    "customer": inv.customer,
                    "risk_value": risk,
                    "confidence": 0.95,
                    "action": f"Send payment reminder to {inv.customer}"
                })

    def get_alerts(self):
        return sorted(
            self.alerts,
            key=lambda x: x["risk_value"],
            reverse=True
        )
