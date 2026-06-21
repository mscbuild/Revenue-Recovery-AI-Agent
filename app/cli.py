from app.core.agent import RevenueRecoveryAgent
from app.services.exporter import Exporter
from app.services.reporter import ReportGenerator


def run(deals, invoices):
    agent = RevenueRecoveryAgent()

    agent.analyze_deals(deals)
    agent.analyze_invoices(invoices)

    alerts = agent.get_alerts()

    report = ReportGenerator().generate(alerts)
    file = Exporter().to_csv(alerts)

    print("\n=== REVENUE RECOVERY REPORT ===")
    print(report)
    print(f"\nCSV exported: {file}")
