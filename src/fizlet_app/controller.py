"""
controller.py
by Man Ly
this file will deal with storing and retrieving data as well as processing and
formating of ouput for the UI
"""

# any imports?
import json
import os

# amu porject-level variables
data_path = "data/"

# function
def store_data(filename: str, data: dict) -> bool:
    """stores data to file and returns if it was succesful"""
    file_path =  "data/" + filename
    data = json.dumps(data)
    try:
        with open(file_path, 'w') as f:
            f.write(data)
    except Exception as e:
        print("sờ tú pịt")
        print(str(e))
        return False
    return True

def get_data(filename: str) -> dict:
    """gets data from file throws exception if not present"""
    file_path = "data/" + filename
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return data
    except Exception as e:
        error = "Error!"
        return error
    
def get_flashcard_set_list() -> list:
    files_list = []
    with os.scandir(data_path) as files:
        for file in files:
            if file.is_file():
                files_list.append(file)
    print(files_list)
    return files_list

if __name__ == "__main__":
    get_file_result = get_data("hello.txt")
    print(get_file_result)
    success = get_flashcard_set_list()
    if success:
        print("did it")
    else:
        print("ops")
