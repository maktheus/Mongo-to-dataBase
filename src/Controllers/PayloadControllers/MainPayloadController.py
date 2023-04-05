import sys

sys.path.append("src")

from Service.PayloadServices.PayloadParseService import PayloadParseService
from Service.PayloadServices.PayloadSeparationService import PayloadSeparationService
from Controllers.DatabaseControllers.DatabaseController import DataBaseController


class payloadController:
    def __init__(self, collections):
        self.collections = collections

    def payloadSeparation(collection):
        payloadSeparation = PayloadSeparationService(collection)
        return payloadSeparation.dataSeparation()

    def payloadParser(dataSeparation):
        payloadParser = PayloadParseService(dataSeparation)
        payloadWise = payloadParser.payloadWiseParser()
        payloadHex = payloadParser.payloadHexParser()
        payloadKS = payloadParser.payloadKSParser()
        return payloadWise, payloadHex, payloadKS
