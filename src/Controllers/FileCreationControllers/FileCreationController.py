import sys

sys.path.append("src")

from Service.FileCreationServices.CsvFileCreationService import CsvFileCreationService


class FileCreationController:
    def createWiseFile(self, pandas_data, file_name):
        CsvFileCreationService.create_csv_file(
            pandas_data, "/home/muchoa/code/cetelli/Mongo_to_h5/saida/wise/", file_name
        )

    def createHexFile(self, pandas_data, file_name):
        CsvFileCreationService.create_csv_file(
            pandas_data, "/home/muchoa/code/cetelli/Mongo_to_h5/saida/hex/", file_name
        )

    def createIteFile(self, pandas_data, file_name):
        CsvFileCreationService.create_csv_file(
            pandas_data, "/home/muchoa/code/cetelli/Mongo_to_h5/saida/ite/", file_name
        )
