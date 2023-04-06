import sys

sys.path.append("src")

from Service.PayloadServices.PayloadParseService import PayloadParseService


class PayloadParserController:
    def payloadParser(payloadSeparated):
        payloadParser = PayloadParseService(payloadSeparated)
        payloadWise = payloadParser.payloadWiseParser()
        payloadHex = payloadParser.payloadHexParser()
        payloadIte = payloadParser.payloadIteParser()
        return payloadWise, payloadHex, payloadIte
