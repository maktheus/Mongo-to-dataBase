import h5py


def WiseToH5(wiseToPandasData):
    x_matrix, y_matrix, z_matrix = WiseToPandas()
    # converter as colunas do DataFrame para tipos suportados pelo HDF5
    x_matrix = x_matrix.astype("float64")
    y_matrix = y_matrix.astype("float64")
    z_matrix = z_matrix.astype("float64")

    with h5py.File("wise_data.h5", "w") as f:
        # criar conjuntos de dados para cada matriz de dados
        f.create_dataset("x", data=x_matrix)
        f.create_dataset("y", data=y_matrix)
        f.create_dataset("z", data=z_matrix)


def HexToH5():
    output_matrix = HexToNumpy()
    with h5py.File("./saida/hex/payloadHex.h5", "w") as f:
        f.create_dataset("payload", data=output_matrix)


def KSToH5():
    output_matrix = KSToNumpy()
    with h5py.File("./saida/ite/payloadITE.h5", "w") as f:
        f.create_dataset("payload", data=output_matrix)


def DataFromTheDatabaseToH5():
    WiseToH5()
    HexToH5()
    KSToH5()
