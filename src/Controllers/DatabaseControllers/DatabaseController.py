import sys
import os
from dotenv import load_dotenv

sys.path.append("src")

from Service.DatabaseServices.ConnectToDatabaseService import (
    ConnectToMongoDataBase,
)
from Service.DatabaseServices.GetCollectionsFromDatabasService import DatabaseService

load_dotenv()

# Recuperar as variáveis de ambiente
MONGO_URL = os.getenv("MONGO_URL")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")


class DataBaseController:
    def __init__(self):
        self.collection = ConnectToMongoDataBase(MONGO_URL, MONGO_DB, MONGO_COLLECTION)
        self.dataBaseService = DatabaseService()

    def getAllDataFromCollection(self):
        data = self.dataBaseService.getAllDataFromCollection(self.collection)
        return data

    def getAllDataFromCollectionFilteredByDate(self, date):
        data = self.dataBaseService.getAllDataFromCollectionFilteredByDate(
            self.collection, date
        )
        return data

    def getAllDataFromCollectionOnPeriod(self, startDate, endDate):
        data = self.dataBaseService.getAllDataFromCollectionOnPeriod(
            self.collection, startDate, endDate
        )
        return data


def main():
    dataBaseController = DataBaseController()
    collection = dataBaseController.getAllDataFromCollection()
    dataBaseController.getAllDataFromCollectionFilteredByDate("2021-10-01")


if __name__ == "__main__":
    main()
