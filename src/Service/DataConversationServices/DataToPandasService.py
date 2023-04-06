import pandas as pd


class DataToPandasService:
    def WiseToPandas(WiseNumpyData):
        x_matrix, y_matrix, z_matrix = WiseNumpyData
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

        return x_df, y_df, z_df

    def HexToPandas(HexNumpyData):
        output_matrix = HexNumpyData
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

    def IteToPandas(KSNumpyData):
        output_matrix = KSNumpyData
        columns = [
            "temperature",
            "frequency",
            "phaseA_voltage",
            "phaseA_current",
            "phaseA_pwr_factor",
            "phaseA_active",
            "phaseA_reactive",
            "phaseA_tc_config",
            "phaseB_voltage",
            "phaseB_current",
            "phaseB_pwr_factor",
            "phaseB_active",
            "phaseB_reactive",
            "phaseB_tc_config",
            "phaseC_voltage",
            "phaseC_current",
            "phaseC_pwr_factor",
            "phaseC_active",
            "phaseC_reactive",
            "phaseC_tc_config",
            "time",
        ]
        df = pd.DataFrame(output_matrix, columns=columns)

        return df
