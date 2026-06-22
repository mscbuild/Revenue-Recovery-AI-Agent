from pydantic import BaseModel
from typing import List, Dict, Any


class Deal(BaseModel):
    id: int
    value: float
    stage: str
    days_in_stage: int


class Invoice(BaseModel):
    id: int
    amount: float
    status: str
    days_overdue: int


class CRMRequest(BaseModel):
    deals: List[Deal]
    invoices: List[Invoice]


class AnalysisResponse(BaseModel):
    risk_report: Dict[str, Any]
    priorities: List[Dict[str, Any]]
    csv: str
