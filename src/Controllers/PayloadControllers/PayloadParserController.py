import sys

sys.path.append("src")

from Service.PayloadServices.PayloadParseService import PayloadParseService


class payloadParserController:
    def __init__(self, payloadSeparated):
        self.payloadSeparated = payloadSeparated

    def payloadParser(self):
        payloadParser = PayloadParseService(self.payloadSeparated)
        payloadWise = payloadParser.payloadWiseParser()
        payloadHex = payloadParser.payloadHexParser()
        payloadKS = payloadParser.payloadKSParser()
        return payloadWise, payloadHex, payloadKS
