import sys

sys.path.append("src")


class dataSeparationService:
    def __init__(self, data):
        self.data = data

    def dataSeparation(self):
        payloadWise = []
        payloadHex = []
        payloadKS = []
        for item in self.data:
            payload = item.get("payload")
            time = item.get("time")
            data = {"time": time, "payload": payload}
            # se tiver bn na str retirar [ ] e separar por virgula
            if "bn" in payload and "74FE48FFFF6D8845" in payload:
                payloadWise.append(data)
            elif "bn" in payload and "74FE48FFFF6D8845" not in payload:
                payloadKS.append(data)
            else:
                payloadHex.append(data)

        return payloadWise, payloadHex, payloadKS
