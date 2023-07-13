import pandas as pd

class PayloadSeparationService:
    def dataSeparationMongo(self, paylod):
        payloadWise = []
        payloadHex = []
        payloadIte = []
        payloadCompressor = []

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

        return payloadWise, payloadHex, payloadIte, payloadCompressor
    
    def dataSeparationCsv(self,payload):
        print("dataSeparationCsv")
        payloadWise = []
        payloadHex = []
        payloadIte = []
        payloadCompressor = []

        print(payload["data"])
        if(payload["data"].empty):
            return payloadWise, payloadHex, payloadIte, payloadCompressor
        
        #separar de vdd
         
        payloadCompressor = payload

        return payloadWise, payloadHex, payloadIte, payloadCompressor


    def dataSeparation(self, payload):
        if(type(payload) == dict):
            payloadWise , payloadHex , payloadIte, payloadCompressor = self.dataSeparationMongo(payload)
            return payloadWise , payloadHex , payloadIte, payloadCompressor
        
        elif(type(payload) == pd.DataFrame):
            payloadWise , payloadHex , payloadIte, payloadCompressor = self.dataSeparationCsv(payload)
            return payloadWise , payloadHex , payloadIte, payloadCompressor
        
