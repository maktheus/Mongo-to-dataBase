from Models.HexModel import HexModel
from Models.WiseModel import WiseModel
from Models.IteModel import IteModel


class DataToModalService:
    def wiseModelParser(payloadWiseParser):
        payloadWise = payloadWiseParser[0]
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
        output = []

        payloadHexParserData = payloadHexParser[1]
        if payloadHexParserData == None:
            return None

        for item in payloadHexParserData:
            payload = item.get("payload")
            Time = item.get("time")
            try:
                # se tiver Accelerometer
                inletPressure = payload["InletPressure"]
                outletPressure = payload["OutletPressure"]
                outletTemperature = payload["OutletTemperature"]
                inverterSpeed = payload["InverterSpeed"]
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
            except:
                pass

        return output

    def iteModelParser(payloadIteParser):
        # {"n": "temperature", "u": "Cel", "v": 52.0}, {"n": "frequency", "u": "Hz", "v": 60.0}, {"n": "phaseA_voltage", "u": "V", "v": 221.5}, {"n": "phaseA_current", "u": "A", "v": 3.5}, {"n": "phaseA_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseA_active", "u": "J", "v": 1362168000.0}, {"n": "phaseA_reactive", "u": "J", "v": 195624000.0}, {"n": "phaseA_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "phaseB_voltage", "u": "V", "v": 221.09999999999999}, {"n": "phaseB_current", "u": "A", "v": 3.6000000000000001}, {"n": "phaseB_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseB_active", "u": "J", "v": 1431288000.0}, {"n": "phaseB_reactive", "u": "J", "v": 159768000.0}, {"n": "phaseB_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "phaseC_voltage", "u": "V", "v": 221.0}, {"n": "phaseC_current", "u": "A", "v": 3.5499999999999998}, {"n": "phaseC_pwr_factor", "u": "/", "v": 0.87000000000000011}, {"n": "phaseC_active", "u": "J", "v": 1368000000.0}, {"n": "phaseC_reactive", "u": "J", "v": 121931999.99999999}, {"n": "phaseC_tc_config", "vs": "POWCT-T16-150-333"}, {"n": "gateway", "vs": "F8033202DF790000"}]', 'timestamp': '2023-02-16 02:31:37'}
        output = []
        for item in payloadIteParser[2]:
            # [{'bn': 'F80332060002BD7B', 'bt': 1676514561}, {'n': 'uplink', 'u': 'count', 'v': 1585}, {'n': 'activation_mode', 'vs': 'ABP'}, {'n': 'datarate', 'vs': 'SF12BW125'}, {'n': 'rssi', 'u': 'dBW', 'v': -90}, {'n': 'snr', 'u': 'dB', 'v': 7.8}, {'n': 'model', 'vs': 'ite11li'}, {'n': 'version', 'vs': '1.0.3.0'}, {'n': 'temperature', 'u': 'Cel', 'v': 52.0}, {'n': 'frequency', 'u': 'Hz', 'v': 60.0}, {'n': 'phaseA_voltage', 'u': 'V', 'v': 221.8}, {'n': 'phaseA_current', 'u': 'A', 'v': 3.5}, {'n': 'phaseA_pwr_factor', 'u': '/', 'v': 0.8600000000000001}, {'n': 'phaseA_active', 'u': 'J', 'v': 1362168000.0}, {'n': 'phaseA_reactive', 'u': 'J', 'v': 195624000.0}, {'n': 'phaseA_tc_config', 'vs': 'POWCT-T16-150-333'}, {'n': 'phaseB_voltage', 'u': 'V', 'v': 221.3}, {'n': 'phaseB_current', 'u': 'A', 'v': 3.6}, {'n': 'phaseB_pwr_factor', 'u': '/', 'v': 0.8799999999999999}, {'n': 'phaseB_active', 'u': 'J', 'v': 1431288000.0}, {'n': 'phaseB_reactive', 'u': 'J', 'v': 159768000.0}, {'n': 'phaseB_tc_config', 'vs': 'POWCT-T16-150-333'}, {'n': 'phaseC_voltage', 'u': 'V', 'v': 221.3}, {'n': 'phaseC_current', 'u': 'A', 'v': 3.55}, {'n': 'phaseC_pwr_factor', 'u': '/', 'v': 0.8700000000000001}, {'n': 'phaseC_active', 'u': 'J', 'v': 1368000000.0}, {'n': 'phaseC_reactive', 'u': 'J', 'v': 121931999.99999999}, {'n': 'phaseC_tc_config', 'vs': 'POWCT-T16-150-333'}, {'n': 'gateway', 'vs': 'F8033202DF790000'}]
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
