from app.services.analyzer import AnalyzerService


class RevenueRecoveryAgent:
    def __init__(self):
        self.analyzer = AnalyzerService()
        self.alerts = []

    def analyze_deals(self, deals):
        self.alerts += self.analyzer.analyze_deals(deals)

    def analyze_invoices(self, invoices):
        self.alerts += self.analyzer.analyze_invoices(invoices)

    def get_alerts(self):
        return sorted(
            self.alerts,
            key=lambda x: x["priority_score"],
            reverse=True
        )
