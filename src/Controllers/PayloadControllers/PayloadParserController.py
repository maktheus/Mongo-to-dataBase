import sys

sys.path.append("src")

from Service.PayloadServices.PayloadParseService import PayloadParseService


class PayloadParserController:
    def payloadParser(payloadSeparated):
        if(payloadSeparated == None):
            #stop the program, and throw an error
            print("payloadSeparated is None")
            return None

        payloadParser = PayloadParseService(payloadSeparated)
        print("payloadParser")
        
                    
        payloadWise = payloadParser.payloadWiseParser()
        payloadHex = payloadParser.payloadHexParser()
        payloadIte = payloadParser.payloadIteParser()
        payloadCompressor = payloadParser.payloadCompressorParser()
        return payloadWise, payloadHex, payloadIte, payloadCompressor
