from dataclasses import dataclass

@dataclass
class Deal:
    id: int
    customer: str
    value: float
    stage: str
    last_contact_days: int


@dataclass
class Invoice:
    invoice_id: int
    customer: str
    amount: float
    overdue_days: int
