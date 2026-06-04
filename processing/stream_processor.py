footfall = 0
transactions = 0

def process(event):
    global footfall, transactions

    if "count" in event:
        footfall += event["count"]
    if "transaction" in event:
        transactions += 1

    return {
        "footfall": footfall,
        "transactions": transactions,
        "conversion": transactions / footfall if footfall else 0
    }
