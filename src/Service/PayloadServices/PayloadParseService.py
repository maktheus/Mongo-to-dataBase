import subprocess
import json
import re
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor


class PayloadParseService:
    def __init__(self, payload):
        self.payload = payload

    def dictCreator(self, payload):
        res =[]

        if(payload == []):
            return []
        
        for item in payload:
            payload = item.get("payload")
            time = item.get("time")
            time = datetime.fromtimestamp(int(re.search(r'\((.*?)\)', time).group(1)[:8],16))
            payload = json.loads(payload)
            res.append({"payload": payload, "time": time})
        
        return res
    
    def payloadHexParser(self):
        print("payload Hex Parser")
        return self.dictCreator(self.payload[3])

    def payloadIteParser(self):
        print("payload Ite Parser")
        return self.dictCreator(self.payload[4])
    
    def payloadCompressorParser(self):
        print("payloadCompressorParser")
        return self.dictCreator(self.payload[5])
    

    def parse_item(self, item):
        payload = item.get("payload")
        time = item.get("time")
        time = datetime.fromtimestamp(int(re.search(r'\((.*?)\)', time).group(1)[:8],16))
        payload = json.loads(payload)
        payloadRaw = payload[6]["vs"]
        payloadDecodifier = subprocess.run(
            ["/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/src/bin/decoder/main-linux", payloadRaw], stdout=subprocess.PIPE
        )

        payloadDecodifier = payloadDecodifier.stdout.decode("utf-8")
        payloadDecodifier = json.loads(payloadDecodifier)
        return {"payload": payloadDecodifier, "time": time}

    def payloadWiseParser(self, payloadWise):
        print("payload Wise Parser")

        with ThreadPoolExecutor() as executor:
            if(self.payload[0] == []):
                return []
            res = list(executor.map(self.parse_item, payloadWise))

        return res
