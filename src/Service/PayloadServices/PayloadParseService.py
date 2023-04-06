import subprocess
import json
from concurrent.futures import ThreadPoolExecutor

class PayloadParseService:
    def __init__(self, payload):
        self.payload = payload

    def parse_item(self, item):
        payload = item.get("payload")
        time = item.get("time")
        payload = json.loads(payload)
        payloadRaw = payload[6]["vs"]
        payloadDecodifier = subprocess.run(
            ["src/bin/decoder/main-linux", payloadRaw], stdout=subprocess.PIPE
        )
        print("payloadDecodifier")
        payloadDecodifier = payloadDecodifier.stdout.decode("utf-8")
        payloadDecodifier = json.loads(payloadDecodifier)
        return {"payload": payloadDecodifier, "time": time}

    def payloadWiseParser(self):
        print("payloadWiseParser")

        with ThreadPoolExecutor() as executor:
            res = list(executor.map(self.parse_item, self.payload[0]))

        return res

    def payloadHexParser(self):
        print("payloadHexParser")
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

    def payloadIteParser(self):
        print("payloadIteParser")
        res = []
        for item in self.payload[2]:
            
            payload = item.get("payload")
            time = item.get("time")
            payload = json.loads(payload)
            res.append({"payload": payload, "time": time})

        return res
