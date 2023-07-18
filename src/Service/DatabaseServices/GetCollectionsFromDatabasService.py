import re
import pandas as pd
import os

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
    
    def getAllDataFromCsv(self, path):
        data = pd.read_csv(path)
        return data

    def getAllDataFromAllCsvs(self,path):
        all_data = []
        for root, dirs, files in os.walk(path):
            for file in files:
                print(file)
                if file.endswith(".csv"):
                    file_path = os.path.join(root, file)
                    data = self.getAllDataFromCsv(file_path)
                    all_data.append(data)
        combined_data = pd.concat(all_data, ignore_index=True)
        return combined_data