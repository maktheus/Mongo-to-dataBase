import sys

sys.path.append("src")

from Controllers.PayloadControllers.PayloadParserController import (
    payloadParserController,
)
from Controllers.PayloadControllers.PayloadSeparationController import (
    payloadSeparationController,
)


class payloadController:
    def __init__(self, collections):
        self.collections = collections

    def payloadTreater(self):
        payloadSeparated = payloadSeparationController.payloadSeparation(
            self.collections
        )
        payloadWise, payloadHex, payloadKS = payloadParserController.payloadParser(
            payloadSeparated
        )
        return payloadWise, payloadHex, payloadKS
