def salesRecord(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "year": item["year"],
        "month": item["month"],
        "sales": item["sales"]
    }

def listOfSalesRecords(item_list) -> list:
    record_list = []
    for item in item_list:
        record_list.append(salesRecord(item))
    return record_list
