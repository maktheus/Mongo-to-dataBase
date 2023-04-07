class CsvFileCreationService:
    def create_csv_file(data, file_path, file_name):
        with open(file_path + file_name, "w") as f:
            data.to_csv(f, index=False, header=True)


# def WiseToCsv():
#     x_matrix, y_matrix, z_matrix = WiseToPandas()
#     columns = [
#         "OAVelocity",
#         "Peakmg",
#         "RMSmg",
#         "Kurtosis",
#         "CrestFactor",
#         "Skewness",
#         "Deviation",
#         "Peak-to-Peak Displacement, Time",
#     ]

#     # criar um arquivo pra cada
#     with open("./saida/wise/x.csv", "w") as f:
#         x_matrix.to_csv(f, index=False, header=True)

#     with open("./saida/wise/y.csv", "w") as f:
#         y_matrix.to_csv(f, index=False, header=True)

#     with open("./saida/wise/z.csv", "w") as f:
#         z_matrix.to_csv(f, index=False, header=True)


# def HexToCsv():
#     output_matrix = HexToPandas()
#     with open("./saida/hex/payloadHex.csv", "w") as f:
#         output_matrix.to_csv(f, index=False, header=True)


# def KSToCsv():
#     output_matrix = KSToPandas()
#     with open("./saida/ite/payloadITE.csv", "w") as f:
#         output_matrix.to_csv(f, index=False, header=True)


# def DataFromTheDatabaseToCsv():
#     WiseToCsv()
#     HexToCsv()
#     KSToCsv()
