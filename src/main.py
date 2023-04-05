from Controllers.DatabaseControllers import DatabaseController
from Controllers.PayloadControllers import MainPayloadController


def main():
    databaseController = DatabaseController()
    collections = databaseController.getAllCollections()

    mainPayloadController = MainPayloadController()
    treatedPayloadData = mainPayloadController.payloadTreater(collections)

    print(treatedPayloadData)


if __name__ == "__main__":
    main()
