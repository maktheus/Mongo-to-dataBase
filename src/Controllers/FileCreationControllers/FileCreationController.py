import sys

sys.path.append("src")

from Service.FileCreationServices.CsvFileCreationService import CsvFileCreationService


class FileCreationController:
    def createWiseFile(self, pandas_data, file_name):
        CsvFileCreationService.create_csv_file(
            pandas_data, "/home/muchoa/willec/Mongo-to-dataBase/saida/wise/", file_name
        )

    def createHexFile(self, pandas_data, file_name):
        CsvFileCreationService.create_csv_file(
            pandas_data, "/home/muchoa/willec/Mongo-to-dataBase/saida/hex/", file_name
        )

    def createIteFile(self, pandas_data, file_name):
        CsvFileCreationService.create_csv_file(
            pandas_data, "/home/muchoa/willec/Mongo-to-dataBase/saida/ite/", file_name
        )

    def createCompressorFile(self, pandas_data, file_name):
        CsvFileCreationService.create_csv_file(
            pandas_data, "/home/muchoa/willec/Mongo-to-dataBase/saida/compressor/", file_name
        )
