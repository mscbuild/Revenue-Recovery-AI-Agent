DEAL_RISK_THRESHOLD = 14
INVOICE_OVERDUE_THRESHOLD = 30


def stalled_deal_risk(deal):
    if deal.last_contact_days > DEAL_RISK_THRESHOLD:
        return deal.value * 0.30
    return 0


def overdue_invoice_risk(invoice):
    if invoice.overdue_days > INVOICE_OVERDUE_THRESHOLD:
        return invoice.amount
    return 0
