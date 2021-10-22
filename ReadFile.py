import json


def parse_json(file_path):
    """
    Takes in filepath and reads file in json format and returns data
    :param file_path: The path of the file's location
    :return: All of the data parsed through
    """

    try: # Opens and loads data
        file = open(file_path, 'r')
        data = json.load(file)
        file.close()
        return data

    except FileNotFoundError:
        print("Filename not found, please check file")
        raise
    except OSError:
        print("Could not open file")