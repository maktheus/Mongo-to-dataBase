import sys

sys.path.append("src")

from Service.PayloadServices.PayloadParseService import PayloadParseService


class payloadParserController:
    def __init__(self, collections):
        self.collections = collections

    def payloadParser(dataSeparation):
        payloadParser = PayloadParseService(dataSeparation)
        payloadWise = payloadParser.payloadWiseParser()
        payloadHex = payloadParser.payloadHexParser()
        payloadKS = payloadParser.payloadKSParser()
        return payloadWise, payloadHex, payloadKS
