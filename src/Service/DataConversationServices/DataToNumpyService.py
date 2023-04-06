import numpy as np


class DataToNumpyService:
    def WiseToNumpy(x_matrix, y_matrix, z_matrix):
        x_matrixNumpy = np.array(x_matrix)
        y_matrixNumpy = np.array(y_matrix)
        z_matrixNumpy = np.array(z_matrix)
        return x_matrixNumpy, y_matrixNumpy, z_matrixNumpy

    def HexToNumpy(payloadHexParser):
        output_matrix = np.array(payloadHexParser)
        return output_matrix

    def KSToNumpy(payloadKSParser):
        output_matrix = np.array(payloadKSParser)
        return output_matrix
