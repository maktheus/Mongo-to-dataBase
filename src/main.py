from Controllers.DatabaseControllers import DatabaseController
from Controllers.PayloadControllers import MainPayloadController


def main():
    databaseController = DatabaseController()
    collections = databaseController.getAllCollections()

    payloadController = MainPayloadController(collections)


if __name__ == "__main__":
    main()
