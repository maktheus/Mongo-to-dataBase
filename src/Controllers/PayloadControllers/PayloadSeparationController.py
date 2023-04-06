import sys

sys.path.append("src")

from Service.PayloadServices.PayloadSeparationService import PayloadSeparationService


class PayloadSeparationController:
    def payloadSeparation(collection):
        payloadSeparation = PayloadSeparationService()
        return payloadSeparation.dataSeparation(collection)
