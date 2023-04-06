class PayloadSeparationService:
    def __init__(self):
        self.payload = []

    def getpayload(self, collection):
        for doc in collection:
            dataPayload = doc.get("payload")
            dataTime = doc.get("timestamp")
            data = {"time": dataTime, "payload": dataPayload}
            self.payload.append(data)

        return self.payload

    def dataSeparation(self, payload):
        payloadWise = []
        payloadHex = []
        payloadIte = []
        for item in payload:
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
