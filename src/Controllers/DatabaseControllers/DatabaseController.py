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
        try:
            self.dataBaseService = DatabaseService()
            self.collection = ConnectToMongoDataBase(MONGO_URL, MONGO_DB, MONGO_COLLECTION)
        except Exception as e:
            print("Erro ao conectar com o banco de dados")
            print(e)

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

    def getAllDataFromCsv(self, path):
        data = self.dataBaseService.getAllDataFromCsv(path)
        return data
    
    def getAllDataFromAllCsvs(self, path):
        print("getAllDataFromAllCsvs")
        data = self.dataBaseService.getAllDataFromAllCsvs(path)
        return data
        


def main():
    dataBaseController = DataBaseController()
    collection = dataBaseController.getAllDataFromCollection()
    dataBaseController.getAllDataFromCollectionFilteredByDate("2021-10-01")


if __name__ == "__main__":
    main()
