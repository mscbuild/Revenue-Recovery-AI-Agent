from app.cli import run
from app.core.models import Deal, Invoice

deals = [
    Deal(1, "Acme Corp", 50000, "Negotiation", 20)
]

invoices = [
    Invoice(1001, "Future Systems", 18000, 45)
]

run(deals, invoices)
