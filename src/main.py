from Controllers.DatabaseControllers.DatabaseController import DataBaseController
from Controllers.PayloadControllers.MainPayloadController import MainPayloadController
from Controllers.DataConvertionControllers.DataConvertionController import (
    DataConvertionController,
)
from Controllers.FileCreationControllers.FileCreationController import FileCreationController
from Service.PandasDataManipulationServices.FullfillDataThatNeverGetService import FullfillDataThatNeverGetService

def main():
    databaseController = DataBaseController()
    # 2023-02-16 02:29:31 to 2023-03-03 18:07:36
    # collectionData = databaseController.getAllDataFromCollectionOnPeriod(
    #     "2023-02-16 02:29:31", "2023-02-16 02:34:42"
    # )
    collectionData = databaseController.getAllDataFromCollection()

    mainPayloadController = MainPayloadController(collectionData)
    treatedPayloadData = mainPayloadController.payloadTreater()

    dataConvertionController = DataConvertionController(treatedPayloadData)
    x_matrix, y_matrix, z_matrix = dataConvertionController.WiseToPandas()
    pandasHexData = dataConvertionController.HexToPandas()
    pandasIteData = dataConvertionController.IteToPandas()

    fullfillDataThatNeverGetService = FullfillDataThatNeverGetService()
    pandasHexData = fullfillDataThatNeverGetService.fullfill(pandasHexData)
    pandasIteData = fullfillDataThatNeverGetService.fullfill(pandasIteData)
    x_matrix = fullfillDataThatNeverGetService.fullfill(x_matrix)
    y_matrix = fullfillDataThatNeverGetService.fullfill(y_matrix)
    z_matrix = fullfillDataThatNeverGetService.fullfill(z_matrix)
  

    fileCreationController = FileCreationController()
    fileCreationController.createWiseFile(x_matrix, "x.csv")
    fileCreationController.createWiseFile(y_matrix,"y.csv")
    fileCreationController.createWiseFile(z_matrix,"z.csv")
    fileCreationController.createHexFile(pandasHexData, "hex.csv")
    fileCreationController.createIteFile(pandasIteData, "ite.csv")
    


if __name__ == "__main__":
    main()
