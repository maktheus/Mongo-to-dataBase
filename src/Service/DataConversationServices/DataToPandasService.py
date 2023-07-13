import pandas as pd


class DataToPandasService:
    def WiseToPandas(WiseNumpyData):
        print("WiseToPandas")
        print(WiseNumpyData[0])
        
        if WiseNumpyData is None or WiseNumpyData[0] == []:
            return None
        x_matrix, y_matrix, z_matrix = WiseNumpyData
        if x_matrix is None or x_matrix == []:
            return None
        
        try:
            x_df = pd.DataFrame(
                x_matrix,
                columns=[
                    "OAVelocity",
                    "Peakmg",
                    "RMSmg",
                    "Kurtosis",
                    "CrestFactor",
                    "Skewness",
                    "Deviation",
                    "Peak-to-Peak Displacement",
                    "Time",
                ],
            )
            y_df = pd.DataFrame(
                y_matrix,
                columns=[
                    "OAVelocity",
                    "Peakmg",
                    "RMSmg",
                    "Kurtosis",
                    "CrestFactor",
                    "Skewness",
                    "Deviation",
                    "Peak-to-Peak Displacement",
                    "Time",
                ],
            )
            z_df = pd.DataFrame(
                z_matrix,
                columns=[
                    "OAVelocity",
                    "Peakmg",
                    "RMSmg",
                    "Kurtosis",
                    "CrestFactor",
                    "Skewness",
                    "Deviation",
                    "Peak-to-Peak Displacement",
                    "Time",
                ],
            )
        except ValueError:
            print("ValueError")
            print(x_matrix)
            print(y_matrix)
            print(z_matrix)
            return [], [], []
        
        return x_df, y_df, z_df

    def HexToPandas(HexNumpyData):
        if HexNumpyData is None or HexNumpyData == []:
            return None
        output_matrix = HexNumpyData
        try:
            df = pd.DataFrame(
                output_matrix,
                columns=[
                    "InletPressure",
                    "OutletPressure",
                    "OutletTemperature",
                    "InverterSpeed",
                    "Time",
                ],
            )
            return df
        except ValueError:
            print("ValueError")
            print(output_matrix)
            return None
        
    def IteToPandas(KSNumpyData):
        if KSNumpyData is None or KSNumpyData == []:
            return None
        output_matrix = KSNumpyData
        try:
            columns = [
                "temperature",
                "frequency",
                "phaseA_voltage",
                "phaseA_current",
                "phaseA_pwr_factor",
                "phaseA_active",
                "phaseA_reactive",
                "phaseB_voltage",
                "phaseB_current",
                "phaseB_pwr_factor",
                "phaseB_active",
                "phaseB_reactive",
                "phaseC_voltage",
                "phaseC_current",
                "phaseC_pwr_factor",
                "phaseC_active",
                "phaseC_reactive",
                "Time",
            ]
            df = pd.DataFrame(output_matrix, columns=columns)
        except ValueError:
            print("ValueError")
            print(output_matrix)
            return None
        return df
    
    def CompressorToPandas(CompressorNumpyData):
        print ("CompressorToPandas")
        
        output_matrix = CompressorNumpyData[3]
        if CompressorNumpyData is None or CompressorNumpyData == []:
            return None
        try:
           
            df = pd.json_normalize(output_matrix)

                

        except ValueError:
            print("ValueError")
            return None
        print(df)
        return df
