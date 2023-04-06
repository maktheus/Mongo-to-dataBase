from Controllers.DatabaseControllers.DatabaseController import DataBaseController
from Controllers.PayloadControllers.MainPayloadController import MainPayloadController
from Controllers.DataConvertionControllers.DataConvertionController import (
    DataConvertionController,
)
from Controllers.FileCreationControllers.FileCreationController import FileCreationController


def main():
    databaseController = DataBaseController()
    # 2023-02-16 02:29:31 to 2023-03-03 18:07:36
    collectionData = databaseController.getAllDataFromCollectionOnPeriod(
        "2023-02-16 02:29:31", "2023-02-16 02:34:42"
    )

    mainPayloadController = MainPayloadController(collectionData)
    treatedPayloadData = mainPayloadController.payloadTreater()

    dataConvertionController = DataConvertionController(treatedPayloadData)
    x_matrix, y_matrix, z_matrix = dataConvertionController.WiseToPandas()
    pandasHexData = dataConvertionController.HexToPandas()
    pandasIteData = dataConvertionController.IteToPandas()

    print(pandasHexData)

    fileCreationController = FileCreationController()
    fileCreationController.createWiseFile(x_matrix, "x.csv")
    fileCreationController.createWiseFile(y_matrix,"y.csv")
    fileCreationController.createWiseFile(z_matrix,"z.csv")
    fileCreationController.createHexFile(pandasHexData, "hex.csv")
    fileCreationController.createIteFile(pandasIteData, "ite.csv")
    


if __name__ == "__main__":
    main()
