import numpy as np


class DataToNumpyService:
    def WiseToNumpy(self, x_matrix, y_matrix, z_matrix):
        x_matrix_data = []
        y_matrix_data = []
        z_matrix_data = []
        for doc in x_matrix:
            x_matrix_data.append(
                [
                    doc.OAVelocity,
                    doc.Peakmg,
                    doc.RMSmg,
                    doc.Kurtosis,
                    doc.CrestFactor,
                    doc.Skewness,
                    doc.Deviation,
                    doc.PeaktoPeakDisplacement,
                    doc.Time,
                ]
            )

        for doc in y_matrix:
            y_matrix_data.append(
                [
                    doc.OAVelocity,
                    doc.Peakmg,
                    doc.RMSmg,
                    doc.Kurtosis,
                    doc.CrestFactor,
                    doc.Skewness,
                    doc.Deviation,
                    doc.PeaktoPeakDisplacement,
                    doc.Time,
                ]
            )

        for doc in z_matrix:
            z_matrix_data.append(
                [
                    doc.OAVelocity,
                    doc.Peakmg,
                    doc.RMSmg,
                    doc.Kurtosis,
                    doc.CrestFactor,
                    doc.Skewness,
                    doc.Deviation,
                    doc.PeaktoPeakDisplacement,
                    doc.Time,
                ]
            )

        x_matrixNumpy = np.array(x_matrix_data)
        y_matrixNumpy = np.array(y_matrix_data)
        z_matrixNumpy = np.array(z_matrix_data)
        return x_matrixNumpy, y_matrixNumpy, z_matrixNumpy

    def HexToNumpy(self, payloadHexParser):
        hex_matrix_data = []
        for doc in payloadHexParser:
            hex_matrix_data.append(
                [
                    doc.InletPressure,
                    doc.OutletPressure,
                    doc.OutletTemperature,
                    doc.InverterSpeed,
                    doc.Time,
                ]
            )
        output_matrix = np.array(hex_matrix_data)
        return output_matrix

    def IteToNumpy(self, payloadIteParser):
        ite_matrix_data = []
        for doc in payloadIteParser:
            ite_matrix_data.append(
                [
                    doc.temperature,
                    doc.frequency,
                    doc.phaseA_voltage,
                    doc.phaseA_current,
                    doc.phaseA_pwr_factor,
                    doc.phaseA_active,
                    doc.phaseA_reactive,
                    doc.phaseA_tc_config,
                    doc.phaseB_voltage,
                    doc.phaseB_current,
                    doc.phaseB_pwr_factor,
                    doc.phaseB_active,
                    doc.phaseB_reactive,
                    doc.phaseB_tc_config,
                    doc.phaseC_voltage,
                    doc.phaseC_current,
                    doc.phaseC_pwr_factor,
                    doc.phaseC_active,
                    doc.phaseC_reactive,
                    doc.phaseC_tc_config,
                    doc.time,
                ]
            )

        output_matrix = np.array(ite_matrix_data)
        return output_matrix
