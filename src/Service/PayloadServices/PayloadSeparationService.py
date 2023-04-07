class PayloadSeparationService:
    def dataSeparation(self, payload):
        payloadWise = []
        payloadHex = []
        payloadIte = []
        for item in payload:
            payload = item.get("payload")
            time = item.get("timestamp")
            data = {"time": time, "payload": payload}
            # se tiver bn na str retirar [ ] e separar por virgula
            if "bn" in payload and "74FE48FFFF6D8845" in payload:
                payloadWise.append(data)
            elif "bn" in payload and "74FE48FFFF6D8845" not in payload:
                payloadIte.append(data)
            else:
                payloadHex.append(data)

        return payloadWise, payloadHex, payloadIte
