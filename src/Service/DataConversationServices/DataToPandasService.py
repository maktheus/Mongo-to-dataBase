import pandas as pd
import concurrent.futures

class DataToPandasService:
    def WiseToPandas(WiseNumpyData):
        print("Wise To Pandas")
       
        x_matrix, y_matrix, z_matrix = WiseNumpyData
        
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
        print("Hex To Pandas Service")
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
            print(df)
            return df    
        except ValueError:
            print("ValueError")
            print(output_matrix)
            return None
        
    def IteToPandas(KSNumpyData):
        print("Ite To Pandas")
        
        
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

        def json_to_pandas(matrix_block):
            try:
                print("Json to pandas")
                dfs = [pd.json_normalize(matrix) for matrix in matrix_block]
                df_block = pd.concat(dfs)
                return df_block
            except ValueError:
                print("ValueError")
                return None

        # Dividir output_matrix em blocos de tamanho 10
        matrix_blocks = [output_matrix[i:i+100] for i in range(0, len(output_matrix), 100)]
        
        # Criando um pool de threads
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Executando json_to_pandas em várias threads
            df_blocks = list(executor.map(json_to_pandas, matrix_blocks))
        
        if df_blocks is None or df_blocks == []:
            return None 
        
        # Combine todos os dataframes resultantes
        
        df = pd.concat(df_blocks)
        
        print("data to pandas compressor")
        return df