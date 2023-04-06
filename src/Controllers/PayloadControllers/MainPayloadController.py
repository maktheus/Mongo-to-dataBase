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
        payloadSeparated = PayloadSeparationController.payloadSeparation(
            self.collections
        )

        payloadWise, payloadHex, payloadIte = PayloadParserController.payloadParser(
            payloadSeparated
        )

        return payloadWise, payloadHex, payloadIte
