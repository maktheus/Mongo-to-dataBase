import sys

sys.path.append("src")

from Service.PayloadServices.PayloadSeparationService import PayloadSeparationService


class payloadSeparationController:
    def __init__(self, collections):
        self.collections = collections

    def payloadSeparation(collection):
        payloadSeparation = PayloadSeparationService(collection)
        return payloadSeparation.dataSeparation()
