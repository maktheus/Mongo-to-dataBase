import pandas as pd
import re 
import traceback
class PayloadSeparationService:
    def __init__(self):
        pass

    
    def dataSeparation(self, payload):
        if(type(payload) == dict):
            payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb = self.dataSeparationMongo(payload)
            return payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb
        
        elif(type(payload) == pd.DataFrame):
            payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb = self.dataSeparationCsv(payload)
            return payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb
        
    
    def dataSeparationMongo(self, paylod):
        payloadWiseComp = []
        payloadWiseExtraction = []
        payloadWiseMotor = []
        payloadHex = []
        payloadIte = []
        payloadUmb = []


        for item in payload:
            payload = item.get("payload")
            time = item.get("timestamp")
            data = {"time": time, "payload": payload}
            # se tiver bn na str retirar [ ] e separar por virgula
            if "bn" in payload and "74FE48FFFF6D8845" in payload:
                payloadWiseExtraction.append(data)
            elif "bn" in payload and "74FE48FFFF6D8845" not in payload:
                payloadIte.append(data)
            else:
                payloadHex.append(data)

        return payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb
    
    def dataSeparationCsv(self,payload):
        print("dataSeparationCsv")
        payloadWiseComp = []
        payloadWiseExtraction = []
        payloadWiseMotor = []
        payloadHex = []
        payloadIte = []
        payloadUmb = []
        
        if(payload["data"].empty):
            return payloadWiseExtraction, payloadHex, payloadIte, payloadUmb       


        for index,item in payload.iterrows():
            try:
                if(item["data"] == "[]"):
                    continue
                #verificar se tem bn
                if("bn" not in item["data"]):
                    payloadUmb.append({"payload" : item["data"] , "time":item["_id"]})
                    continue

                bnValue =   re.findall(r'"bn":"([^"]*)"', item["data"])[0]

                if(bnValue == "HEXA0242AC120002"):
                    payloadHex.append({"payload" : item["data"] , "time":item["_id"]})
                elif(bnValue == "F80332060002BD7B"):
                    payloadIte.append({"payload" : item["data"] , "time":item["_id"]})
                elif(bnValue == "74FE48FFFF6D8845"):
                    payloadWiseExtraction.append({"payload" : item["data"] , "time":item["_id"]})
                elif(bnValue == "74FE48FFFF7A1BEE"):
                    payloadWiseMotor.append({"payload" : item["data"] , "time":item["_id"]})
                elif(bnValue == "74FE48FFFF6D89FF"):
                    payloadWiseComp.append({"payload" : item["data"] , "time":item["_id"]})
                else:
                    payloadUmb.append({"payload" : item["data"] , "time":item["_id"]})

            except Exception as e:
                print (item)
                print(traceback.format_exc())
                pass

        return payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb


