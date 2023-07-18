import traceback


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
    try:
        print("==================================== 🚀 database connection 🚀 ====================================")
        databaseController = DataBaseController()
        collectionDataHex = databaseController.getAllDataFromCollection()
        # 2023-02-16 02:29:31 to 2023-03-03 18:07:36
        # collectionDataHex = databaseController.getAllDataFromCollectionOnPeriod(
        #     "2023-03-07 02:29:31", "2023-04-03 3:29:31"
        # )
    except Exception as e:
        
        print("Error in database connection")
        print("Error:",e)

    try:
        print("==================================== 🚀 csv connection 🚀 ====================================")
        
        # collectionDataHex = databaseController.getAllDataFromCsv("/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/extraction_11072023 (1)/extracao_11072023/hexa_extraction_11072023.csv")
        # collectionDataIte = databaseController.getAllDataFromCsv("/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/extraction_11072023 (1)/extracao_11072023/ite_extraction_11072023.csv")
        # collectionDataUmb = databaseController.getAllDataFromCsv("/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/extraction_11072023 (1)/extracao_11072023/umb_extraction_11072023.csv")
        # collectionDataWiseCompressor = databaseController.getAllDataFromCsv("/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/extraction_11072023 (1)/extracao_11072023/wise_compressor_extraction_11072023.csv")
        # collectionDataWiseExtraction = databaseController.getAllDataFromCsv("/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/extraction_11072023 (1)/extracao_11072023/wise_extraction_11072023.csv")
        # collectionDataWiseMotor = databaseController.getAllDataFromCsv("/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/extraction_11072023 (1)/extracao_11072023/wise_motor_extraction_11072023.csv")

        collectionData = databaseController.getAllDataFromAllCsvs("/home/muchoa/willec/tratamentoBaseDeDados/Mongo-to-dataBase/extraction_11072023 (1)/extracao_11072023")
    except Exception as e:
        print("Error in csv connection")


    try:
        print("==================================== 🚀 payload treatment 🚀 ==================================== ")
        mainPayloadController = MainPayloadController(collectionData)
        treatedPayloadData = mainPayloadController.payloadTreater()
            
    except Exception as e:
        print("Error:",e)
        print("Error in payload treatment")
        traceback.print_exc()
        exit()

    try:
        print("==================================== 🚀 data convertion 🚀 ==================================== ")
        dataConvertionController = DataConvertionController(treatedPayloadData)
        x_matrix, y_matrix, z_matrix = dataConvertionController.WiseToPandas()
        pandasHexData = dataConvertionController.HexToPandas()
        pandasIteData = dataConvertionController.IteToPandas()
        pandasCompressorData = dataConvertionController.CompressorToPandas()
    except Exception as e:
        print("Error in data convertion")
        print("Error:",e)
        traceback.print_exc()
        exit()


    try:
        print("==================================== 🚀 data createation 🚀 ==================================== ")
        # payloadWiseExtraction, payloadWiseMotor, payloadWiseComp ,payloadHex, payloadIte, payloadUmb
        fileCreationController = FileCreationController()
        fileCreationController.createWiseFile(x_matrix, "x.csv")
        fileCreationController.createWiseFile(y_matrix, "y.csv")
        fileCreationController.createWiseFile(z_matrix, "z.csv")

        # fileCreationController.createWiseFile(x_matrix, "x.csv")
        # fileCreationController.createWiseFile(y_matrix, "y.csv")
        # fileCreationController.createWiseFile(z_matrix, "z.csv")

        # fileCreationController.createWiseFile(x_matrix, "x.csv")
        # fileCreationController.createWiseFile(y_matrix, "y.csv")
        # fileCreationController.createWiseFile(z_matrix, "z.csv")


        fileCreationController.createHexFile(pandasHexData, "hex.csv")
        fileCreationController.createIteFile(pandasIteData, "ite.csv")
        fileCreationController.createCompressorFile(pandasCompressorData, "compressor.csv")
    except Exception as e:
        
        print("Error in file creation")
        print("Error:",e)
        traceback.print_exc()
        exit()

    try:
        print("==================================== 🚀 fullfill data 🚀 ====================================")
        fullfillDataThatNeverGetService = FullfillDataThatNeverGetService()
        pandasHexData = fullfillDataThatNeverGetService.fullfill("/home/muchoa/willec/Mongo-to-dataBase/saida/hex/hex.csv")
        x_matrix = fullfillDataThatNeverGetService.fullfill("/home/muchoa/willec/Mongo-to-dataBase/saida/wise/x.csv")
        y_matrix = fullfillDataThatNeverGetService.fullfill("/home/muchoa/willec/Mongo-to-dataBase/saida/wise/y.csv")
        z_matrix = fullfillDataThatNeverGetService.fullfill("/home/muchoa/willec/Mongo-to-dataBase/saida/wise/z.csv")
        pandasIteData = fullfillDataThatNeverGetService.fullfill("/home/muchoa/willec/Mongo-to-dataBase/saida/ite/ite.csv")

        fileCreationController.createWiseFile(x_matrix, "xFullfilled.csv")
        fileCreationController.createWiseFile(y_matrix, "yFullfilled.csv")
        fileCreationController.createWiseFile(z_matrix, "zFullfilled.csv")
        fileCreationController.createHexFile(pandasHexData, "hexFullfilled.csv")
        fileCreationController.createIteFile(pandasIteData, "iteFullfilled.csv")
    except Exception as e:
        print("Error in fullfill data")
        print("Error:",e)

if __name__ == "__main__":
    main()
