import sys

sys.path.append("src")

from Controllers.PayloadControllers.PayloadParserController import (
    PayloadParserController,
)
from Controllers.PayloadControllers.PayloadSeparationController import (
    PayloadSeparationController,
)


class MainPayloadController:
    def __init__(self, collections):
        self.collections = collections

    def payloadTreater(self):
        print("payloadTreater")
        payloadSeparated = PayloadSeparationController.payloadSeparation(
            self.collections
        )
        print("payloadSeparated")

        payloadWise, payloadHex, payloadIte, payloadCompressor = PayloadParserController.payloadParser(
            payloadSeparated
        )
        print("payloadParsed")
        return payloadWise, payloadHex, payloadIte, payloadCompressor
