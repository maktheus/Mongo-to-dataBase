import sys

sys.path.append("src")

from Service.PayloadServices.PayloadParseService import PayloadParseService


class PayloadParserController:
    def payloadParser(payloadSeparated):
        print("=============================================== Payload Parser Controller ===============================================")
        if(payloadSeparated == None):
            #stop the program, and throw an error

            print("payloadSeparated is None")
            return None

        payloadParser = PayloadParseService(payloadSeparated)
        
                    
        payloadWiseExtraction = payloadParser.payloadWiseParser(payloadSeparated[0])
        payloadWiseMotor = payloadParser.payloadWiseParser(payloadSeparated[1])
        payloadWiseComp =   payloadParser.payloadWiseParser(payloadSeparated[2])
        payloadHex = payloadParser.payloadHexParser()
        payloadIte = payloadParser.payloadIteParser()
        payloadUmb = payloadParser.payloadCompressorParser()

        return  payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb
