from fastapi import FastAPI
from app.core.agent import RevenueRecoveryAgent

app = FastAPI(title="Revenue Recovery AI")

@app.post("/analyze")
def analyze(payload: dict):
    agent = RevenueRecoveryAgent()

    agent.analyze_deals(payload.get("deals", []))
    agent.analyze_invoices(payload.get("invoices", []))

    return {
        "alerts": agent.get_alerts()
    }
