import subprocess
import json
import re
from datetime import datetime
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
            ["/home/muchoa/willec/Mongo-to-dataBase/src/bin/decoder/main-linux", payloadRaw], stdout=subprocess.PIPE
        )

        payloadDecodifier = payloadDecodifier.stdout.decode("utf-8")
        payloadDecodifier = json.loads(payloadDecodifier)
        return {"payload": payloadDecodifier, "time": time}

    def payloadWiseParser(self):
        print("payloadWiseParser")

        with ThreadPoolExecutor() as executor:
            if(self.payload[0] == []):
                return []
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
    
    def payloadCompressorParser(self):
        print("payloadCompressorParser")
        pandaDataFrame = self.payload[3]
        res = []
        for index, row in pandaDataFrame.iterrows():
            payload = row["data"]
            time = datetime.fromtimestamp(int(re.search(r'\((.*?)\)', row["_id"]).group(1)[:8],16))
            payload = json.loads(payload)
           
            res.append({"payload": payload, "time": time})

        
        return res
