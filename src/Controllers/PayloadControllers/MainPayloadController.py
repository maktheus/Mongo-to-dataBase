import sys

sys.path.append("src")

from Controllers.PayloadControllers.PayloadParserController import (
    payloadParserController,
)
from Controllers.PayloadControllers.PayloadSeparationController import (
    payloadSeparationController,
)


class MainPayloadController:
    def __init__(self, collections):
        self.collections = collections

    def payloadTreater(self):
        payloadSeparated = payloadSeparationController.payloadSeparation(
            self.collections
        )
        payloadWise, payloadHex, payloadIte = payloadParserController.payloadParser(
            payloadSeparated
        )
        return payloadWise, payloadHex, payloadIte
