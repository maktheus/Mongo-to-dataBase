import sys

sys.path.append("src")

from Service.PayloadServices.PayloadSeparationService import PayloadSeparationService


class PayloadSeparationController:
    def payloadSeparation(collection):
        payloadSeparation = PayloadSeparationService()
        payload = payloadSeparation.getpayload(collection)
        return payloadSeparation.dataSeparation(payload)
