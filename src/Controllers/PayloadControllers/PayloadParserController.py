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
        payloadIte = payloadParser.payloadIteParser()
        return payloadWise, payloadHex, payloadIte
