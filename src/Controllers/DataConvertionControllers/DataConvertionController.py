import sys

sys.path.append("src")

from Service.DataConversationServices.DataToNumpyService import DataToNumpyService
from Service.DataConversationServices.DataToModelService import DataToModalService


class DataConvertionController:
    def __init__(self, data):
        self.data = data
        self.dataConvertionService = DataToNumpyService()

    def WiseToNumpy(self):
        x_matrix, y_matrix, z_matrix = DataToModalService.wiseModelParser(self.data)
        return x_matrix, y_matrix, z_matrix

    def HexToNumpy(self):
        listHex = DataToModalService.hexWiseParser(self.data)
        return listHex

    def IteToNumpy(self):
        listIte = DataToModalService.iteWiseParser(self.data)
        return listIte
