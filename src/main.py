from Controllers.DatabaseControllers.DatabaseController import DataBaseController
from Controllers.PayloadControllers.MainPayloadController import MainPayloadController
from Controllers.DataConvertionControllers.DataConvertionController import (
    DataConvertionController,
)
from Controllers.FileCreationControllers.FileCreationController import (
    FileCreationController,
)
from Service.PandasDataManipulationServices.FullfillDataThatNeverGetService import (
    FullfillDataThatNeverGetService,
)


def main():
    databaseController = DataBaseController()
    # 2023-02-16 02:29:31 to 2023-03-03 18:07:36
    # collectionData = databaseController.getAllDataFromCollectionOnPeriod(
    #     "2023-02-16 02:29:31", "2023-02-16 3:29:31"
    # )
    collectionData = databaseController.getAllDataFromCollection()

    print("collectionData")

    mainPayloadController = MainPayloadController(collectionData)
    treatedPayloadData = mainPayloadController.payloadTreater()

    print("treatedPayloadData")
    dataConvertionController = DataConvertionController(treatedPayloadData)
    x_matrix, y_matrix, z_matrix = dataConvertionController.WiseToPandas()
    pandasHexData = dataConvertionController.HexToPandas()
    pandasIteData = dataConvertionController.IteToPandas()

    print("pandasHexData")

    fileCreationController = FileCreationController()
    fileCreationController.createWiseFile(x_matrix, "x.csv")
    fileCreationController.createWiseFile(y_matrix, "y.csv")
    fileCreationController.createWiseFile(z_matrix, "z.csv")
    fileCreationController.createHexFile(pandasHexData, "hex.csv")
    fileCreationController.createIteFile(pandasIteData, "ite.csv")

    fullfillDataThatNeverGetService = FullfillDataThatNeverGetService()
    pandasHexData = fullfillDataThatNeverGetService.fullfill("/home/muchoa/code/cetelli/Mongo_to_h5/saida/hex/hex.csv")
    x_matrix = fullfillDataThatNeverGetService.fullfill("/home/muchoa/code/cetelli/Mongo_to_h5/saida/wise/x.csv")
    y_matrix = fullfillDataThatNeverGetService.fullfill("/home/muchoa/code/cetelli/Mongo_to_h5/saida/wise/y.csv")
    z_matrix = fullfillDataThatNeverGetService.fullfill("/home/muchoa/code/cetelli/Mongo_to_h5/saida/wise/z.csv")
    pandasIteData = fullfillDataThatNeverGetService.fullfill("/home/muchoa/code/cetelli/Mongo_to_h5/saida/ite/ite.csv")

    fileCreationController.createWiseFile(x_matrix, "xFullfilled.csv")
    fileCreationController.createWiseFile(y_matrix, "yFullfilled.csv")
    fileCreationController.createWiseFile(z_matrix, "zFullfilled.csv")
    fileCreationController.createHexFile(pandasHexData, "hexFullfilled.csv")
    fileCreationController.createIteFile(pandasIteData, "iteFullfilled.csv")
    



if __name__ == "__main__":
    main()
