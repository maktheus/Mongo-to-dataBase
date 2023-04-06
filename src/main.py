from Controllers.DatabaseControllers.DatabaseController import DataBaseController
from Controllers.PayloadControllers.MainPayloadController import MainPayloadController


def main():
    databaseController = DataBaseController()
    #2023-02-16 02:29:31 to 2023-03-03 18:07:36
    collectionData = databaseController.getAllDataFromCollectionOnPeriod(
        "2023-02-16 02:29:31", "2023-03-03 18:07:36"
    )


    mainPayloadController = MainPayloadController(collectionData)
    treatedPayloadData = mainPayloadController.payloadTreater()

    print(treatedPayloadData)


if __name__ == "__main__":
    main()
