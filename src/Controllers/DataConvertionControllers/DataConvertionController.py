import sys

sys.path.append("src")

from Service.DataConversationServices.DataToNumpyService import DataToNumpyService
from Service.DataConversationServices.DataToModelService import DataToModalService
from Service.DataConversationServices.DataToPandasService import DataToPandasService


class DataConvertionController:
    def __init__(self, data):
        self.data = data
        self.dataConvertionService = DataToNumpyService()

    def WiseToPandas(self):
        x_matrix, y_matrix, z_matrix = DataToModalService.wiseModelParser(self.data)
        numpy_matrix = self.dataConvertionService.WiseToNumpy(
            x_matrix, y_matrix, z_matrix
        )
        pandas_matrix = DataToPandasService.WiseToPandas(numpy_matrix)
        return pandas_matrix

    def HexToPandas(self):
        listHex = DataToModalService.hexWiseParser(self.data)
        numpy_hex = self.dataConvertionService.HexToNumpy(listHex)
        pandas_hex = DataToPandasService.HexToPandas(numpy_hex)

        return pandas_hex

    def IteToPandas(self):
        listIte = DataToModalService.iteModelParser(self.data)
        numpy_ite = self.dataConvertionService.IteToNumpy(listIte)
        pandas_ite = DataToPandasService.IteToPandas(numpy_ite)
        return pandas_ite
    
    def CompressorToPandas(self):
        #json to pandas
        pandas_compressor = DataToPandasService.CompressorToPandas(self.data)

        return pandas_compressor

