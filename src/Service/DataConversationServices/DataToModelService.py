import traceback
import json
from Models.HexModel import HexModel
from Models.WiseModel import WiseModel
from Models.IteModel import IteModel


class DataToModalService:
    def __init__(self):
        print("Data To Modal Service")
        pass

    def wiseModelParser(payloadWiseParser):
        print("Wise Model Parser")
        payloadWise = payloadWiseParser
        x_matrix = []
        y_matrix = []
        z_matrix = []
        for item in payloadWise:
            try:
                payload = item["payload"]
                Time = item["time"]
                # se tiver Accelerometer
                if "Accelerometer" in payload:
                    acc = payload["Accelerometer"]
                    x = acc["X-Axis"]
                    y = acc["Y-Axis"]
                    z = acc["Z-Axis"]
                    wiseModelX = WiseModel(
                        x["OAVelocity"],
                        x["Peakmg"],
                        x["RMSmg"],
                        x["Kurtosis"],
                        x["CrestFactor"],
                        x["Skewness"],
                        x["Deviation"],
                        x["Peak-to-Peak Displacement"],
                        Time,
                    )
                    wiseModelY = WiseModel(
                        y["OAVelocity"],
                        y["Peakmg"],
                        y["RMSmg"],
                        y["Kurtosis"],
                        y["CrestFactor"],
                        y["Skewness"],
                        y["Deviation"],
                        y["Peak-to-Peak Displacement"],
                        Time,
                    )
                    wiseModelZ = WiseModel(
                        z["OAVelocity"],
                        z["Peakmg"],
                        z["RMSmg"],
                        z["Kurtosis"],
                        z["CrestFactor"],
                        z["Skewness"],
                        z["Deviation"],
                        z["Peak-to-Peak Displacement"],
                        Time,
                    )
                    x_matrix.append(wiseModelX)
                    y_matrix.append(wiseModelY)
                    z_matrix.append(wiseModelZ)
            except:
                pass

        return x_matrix, y_matrix, z_matrix

    def hexWiseParser(payloadHexParser):
        # payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb
        print("Hex Wise Parser")
        output = []

        payloadHexParserData = payloadHexParser[3]

        if payloadHexParserData == None:
            print("payloadHexParserData is None")
            return None

        for item in payloadHexParserData:
  
            payload = item.get("payload")[1].get("properties")
            Time = item.get("time")
            try:
                # se tiver Accelerometer
                
                inletPressure = payload[0].get("value")
                outletPressure = payload[1].get("value")
                outletTemperature = payload[9].get("value")
                inverterSpeed = payload[26].get("value")
                if (
                    inletPressure is not None
                    and outletPressure is not None
                    and outletTemperature is not None
                    and inverterSpeed is not None
                ):
                    hexModel = HexModel(
                        inletPressure,
                        outletPressure,
                        outletTemperature,
                        inverterSpeed,
                        Time,
                    )
                    output.append(hexModel)
            except Exception as e:
                print("Error in Hex Wise Parser")
                print("Error:",e)
                print("Traceback:",traceback.print_exc())
                pass

        return output

    def iteModelParser(payloadIteParser):

        print("Ite Model Parser")
        output = []
        #  payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb
        if(payloadIteParser == []):
            return []

        for item in payloadIteParser[4]:
            try:
                payload = item.get("payload")
                Time = item.get("time")
                temperatura = payload[8].get("v")
                frequencia = payload[9].get("v")
                faseA_tensao = payload[10].get("v")
                faseA_corrente = payload[11].get("v")
                faseA_fator_potencia = payload[12].get("v")
                faseA_ativa = payload[13].get("v")
                faseA_reativa = payload[14].get("v")
                faseB_tensao = payload[16].get("v")
                faseB_corrente = payload[17].get("v")
                faseB_fator_potencia = payload[18].get("v")
                faseB_ativa = payload[19].get("v")
                faseB_reativa = payload[20].get("v")
                faseC_tensao = payload[22].get("v")
                faseC_corrente = payload[23].get("v")
                faseC_fator_potencia = payload[24].get("v")
                faseC_ativa = payload[25].get("v")
                faseC_reativa = payload[26].get("v")
            except IndexError:
                print("IndexError in Ite Model Parser")
                pass

            iteModel = IteModel(
                temperatura,
                frequencia,
                faseA_tensao,
                faseA_corrente,
                faseA_fator_potencia,
                faseA_ativa,
                faseA_reativa,
                faseB_tensao,
                faseB_corrente,
                faseB_fator_potencia,
                faseB_ativa,
                faseB_reativa,
                faseC_tensao,
                faseC_corrente,
                faseC_fator_potencia,
                faseC_ativa,
                faseC_reativa,
                Time,
            )
            output.append(iteModel)

        return output
