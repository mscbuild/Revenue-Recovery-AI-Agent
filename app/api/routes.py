from fastapi import APIRouter
from app.api.schemas import CRMRequest
from app.core.agent import RevenueRecoveryAgent

router = APIRouter()

agent = RevenueRecoveryAgent()


@router.post("/analyze")
def analyze(payload: CRMRequest):
    result = agent.run(payload.model_dump())
    return result
