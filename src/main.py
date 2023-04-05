from Controllers.DatabaseControllers.DatabaseController import DataBaseController
from Controllers.PayloadControllers.MainPayloadController import MainPayloadController


def main():
    databaseController = DataBaseController()
    collections = databaseController.getAllDataFromCollection()

    # collection = databaseController.getCollectionByName("Wise")
    # collection = databaseController.getCollectionByName("Hex")
    # collection = databaseController.getCollectionByName("Ks")
    # collection = databaseController.getCollectionByName("Ks")

    mainPayloadController = MainPayloadController(collections)
    treatedPayloadData = mainPayloadController.payloadTreater()

    print(treatedPayloadData)


if __name__ == "__main__":
    main()
