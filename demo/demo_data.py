def get_sample_payload():
    return {
        "deals": [
            {"id": 1, "value": 12000, "stage": "stalled", "days_in_stage": 45},
            {"id": 2, "value": 5000, "stage": "negotiation", "days_in_stage": 10}
        ],
        "invoices": [
            {"id": 101, "amount": 3000, "status": "overdue", "days_overdue": 20}
        ]
    }
