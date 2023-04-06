import sys

sys.path.append("src")

from Service.DataConversationServices.DataToNumpyService import DataToNumpyService


class dataConvertionController:
    def __init__(self, data):
        self.data = data
        self.dataConvertionService = DataToNumpyService()

    def WiseToNumpy(self):
        x_matrix, y_matrix, z_matrix = self.dataConvertionService.WiseToNumpy(self.data)
        return x_matrix, y_matrix, z_matrix

    def HexToNumpy(self):
        listHex = self.dataConvertionService.HexToNumpy(self.data)
        return listHex

    def IteToNumpy(self):
        listIte = self.dataConvertionService.IteToNumpy(self.data)
        return listIte
