import subprocess
import json


class PayloadParseService:
    def __init__(self, payload):
        self.payload = payload

    def payloadWiseParser(self):
        res = []
        for item in self.payload[0]:
            payload = item.get("payload")
            time = item.get("time")
            payload = json.loads(payload)
            payloadRaw = payload[6]["vs"]
            payloadDecodifier = subprocess.run(
                ["src/bin/decoder/main-linux", payloadRaw], stdout=subprocess.PIPE
            )
            payloadDecodifier = payloadDecodifier.stdout.decode("utf-8")
            payloadDecodifier = json.loads(payloadDecodifier)
            res.append({"payload": payloadDecodifier, "time": time})
        return res

    def payloadHexParser(self):
        res = []
        for item in self.payload[1]:
            payload = item.get("payload")
            time = item.get("time")
            try:
                payload = json.loads(payload)
            except json.decoder.JSONDecodeError:
                pass
            res.append({"payload": payload, "time": time})

        return res

    def payloadKSParser(self):
        res = []
        for item in self.payload[2]:
            payload = item.get("payload")
            time = item.get("time")
            payload = json.loads(payload)
            res.append({"payload": payload, "time": time})

        return res
