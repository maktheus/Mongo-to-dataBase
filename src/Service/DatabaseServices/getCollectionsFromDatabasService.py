import datetime


class DatabaseService:
    def __init__(self):
        pass

    def getAllDataFromCollection(self, collection):
        docs = collection.find({}, {"_id": False})
        return docs

    def getAllDataFromCollectionFilteredByDate(self, collection, date):
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        start_date = datetime.datetime.combine(date, datetime.time.min)
        end_date = datetime.datetime.combine(date, datetime.time.max)

        docs = collection.find(
            {"date_field": {"$gte": start_date, "$lte": end_date}}, {"_id": False}
        )
        return docs
