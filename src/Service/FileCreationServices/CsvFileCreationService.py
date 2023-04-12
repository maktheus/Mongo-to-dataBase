import os
class CsvFileCreationService:
    def create_csv_file(data, file_path, file_name):
        # se a pasta não existir, cria
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        with open(file_path + file_name, "w") as f:
            data.to_csv(f, index=False, header=True)