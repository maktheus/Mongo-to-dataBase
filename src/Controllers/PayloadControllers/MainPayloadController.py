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
        print("============================== Payload Treater Controller =============================")
        print("Payload Separation")
        payloadSeparated = PayloadSeparationController.payloadSeparation(
            self.collections
        )

        print("Payload Parser")

        payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb = PayloadParserController.payloadParser(
            payloadSeparated
        )

        return payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb

