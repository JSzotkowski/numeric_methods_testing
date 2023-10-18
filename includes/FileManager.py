from json import dump, load


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def save_list_to_file(self, data_list):
        try:
            with open(self.filename, 'w') as file:
                for item in data_list:
                    file.write(str(item) + '\n')
            print(f"Data saved successfully to {self.filename}.")
        except Exception as e:
            print(f"Error while saving data to {self.filename}:", e)

    def load_list_from_file(self):
        data_list = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    data_list.append(line.strip())
            print(f"Data loaded successfully from {self.filename}.")
            return data_list
        except Exception as e:
            print(f"Error while loading data from {self.filename}:", e)
            return []

    def save_json_to_file(self, data_dict):
        try:
            with open(self.filename, 'w') as file:
                dump(data_dict, file, indent=4)
            print(f"JSON data saved successfully to {self.filename}.")
        except Exception as e:
            print(f"Error while saving JSON data to {self.filename}:", e)

    def load_json_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                data_dict = load(file)
            print(f"JSON data loaded successfully from {self.filename}.")
            return data_dict
        except Exception as e:
            print(f"Error while loading JSON data from {self.filename}:", e)
            return {}


if __name__ == '__main__':
    # Create an instance of FileManager
    file_manager = FileManager("/home/jiri/PycharmProjects/numeric_methods_testing/resources/FileManagerTestFile.txt")

    # Example data list
    data_to_save = ["Line 1", "Line 2", "Line 3"]

    # Save data list to file
    file_manager.save_list_to_file(data_to_save)

    # Load data list from file
    loaded_data = file_manager.load_list_from_file()

    # Print loaded data
    assert data_to_save == loaded_data

    # Example usage
    file_manager = FileManager("/home/jiri/PycharmProjects/numeric_methods_testing/resources/FileManagerTestFile.json")

    # Save JSON dictionary to file
    json_data = {"name": "John", "age": 30, "city": "New York", "data": {"money": 0, "attractiveness": 0}}
    file_manager.save_json_to_file(json_data)

    # Load JSON dictionary from file
    loaded_json_data = file_manager.load_json_from_file()

    assert json_data == loaded_json_data
    assert json_data["data"]["money"] == loaded_json_data["data"]["money"]
