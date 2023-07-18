import sys
import os
sys.path.append("src")

from Service.FileCreationServices.CsvFileCreationService import CsvFileCreationService


class FileCreationController:

    def __init__(self):
        #get the present directory
        self.presentDirectory = os.getcwd()

    def createWiseFile(self, pandas_data, file_name):
        print("create Wise File")
        if(pandas_data is None):
            print("pandas_data is None ")
            return
        CsvFileCreationService.create_csv_file(
            pandas_data, self.presentDirectory+"/saida/bombaDePressao/wise/", file_name
        )
    
    def createWiseFileMotor(self, pandas_data, file_name):
        print("create Wise File Motor")
        if(pandas_data is None):
            print("pandas_data is None ")
            return
        CsvFileCreationService.create_csv_file(
            pandas_data, self.presentDirectory+"/saida/bombaDePressao/wiseMotor/", file_name
        )
    
    def createWiseFileComp(self, pandas_data, file_name):
        print("create Wise File Comp")
        if(pandas_data is None):
            print("pandas_data is None ")
            return
        CsvFileCreationService.create_csv_file(
            pandas_data, self.presentDirectory+"/saida/compressor/wiseComp/", file_name
        )

    def createHexFile(self, pandas_data, file_name):
        print("create Hex File")
        print(pandas_data)
        if(pandas_data is None):
            print("pandas_data is None ")
            return
        
        CsvFileCreationService.create_csv_file(
            pandas_data, self.presentDirectory+"/saida/bombaDePressao/hex/", file_name
        )

    def createIteFile(self, pandas_data, file_name):
        print("create Ite File")

        if(pandas_data is None):
            print("pandas_data is None ")
            return
        
        CsvFileCreationService.create_csv_file(
            pandas_data, self.presentDirectory+"/saida/bombaDePressao/ite/", file_name
        )

    def createCompressorFile(self, pandas_data, file_name):
        print("create Compressor File")
        if(pandas_data is None):
            print("pandas_data is None ")
            return
        CsvFileCreationService.create_csv_file(
            pandas_data, self.presentDirectory+"/saida/compressor/UMB", file_name
        )
