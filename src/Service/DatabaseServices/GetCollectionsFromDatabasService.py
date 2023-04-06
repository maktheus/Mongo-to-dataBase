import re
from datetime import datetime, date, time


class DatabaseService:
    def __init__(self):
        pass

    def getAllDataFromCollection(self, collection):
        docs = collection.find({}, {"_id": False})
        return docs

    def getAllDataFromCollectionFilteredByDate(self, collection, date):
        date = datetime.strptime(date, "%Y-%m-%d").date()
        start_date = datetime.combine(date, time.min)
        end_date = datetime.combine(date, time.max)

        docs = collection.find(
            {"date_field": {"$gte": start_date, "$lte": end_date}}, {"_id": False}
        )
        return docs

    def getAllDataFromCollectionOnPeriod(self, collection, start_date_str, end_date_str):
        query = {"timestamp": {"$gte": start_date_str, "$lte": end_date_str}}
        projection = {"_id": False}
        cursor = collection.find(query, projection)
        return cursor
