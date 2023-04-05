import sys

sys.path.append("src")


class PayloadSeparationService:
    def __init__(self, collection):
        self.collection = collection

    def dataSeparation(self):
        payloadWise = []
        payloadHex = []
        payloadIte = []
        for item in self.collection:
            payload = item.get("payload")
            time = item.get("time")
            data = {"time": time, "payload": payload}
            # se tiver bn na str retirar [ ] e separar por virgula
            if "bn" in payload and "74FE48FFFF6D8845" in payload:
                payloadWise.append(data)
            elif "bn" in payload and "74FE48FFFF6D8845" not in payload:
                payloadIte.append(data)
            else:
                payloadHex.append(data)

        return payloadWise, payloadHex, payloadIte
