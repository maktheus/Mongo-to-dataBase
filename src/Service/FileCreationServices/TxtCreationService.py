class SaveRawDataController:
    def saveRawDataInFile(collection):
        with open("saida/raw/dados.txt", "w") as outfile:
            for doc in collection:
                outfile.write(str(doc))
                outfile.write("\n")
