class ReportGenerator:
    def generate(self, alerts):
        total = sum(a["risk_value"] for a in alerts)

        report = {
            "total_risk": total,
            "alert_count": len(alerts),
            "alerts": alerts
        }

        return report
