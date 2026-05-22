"""
controller.py
by Man Ly
this file will deal with storing and retrieving data as well as processing and
formating of ouput for the UI
"""
# any imports?

# amu porject-level variables

# function
def store_data(filename: str, data: str) -> bool:
    """stores data to file and returns if it was succesful"""
    file_path =  "data/" + filename
    try:
        with open(file_path, 'w') as f:
            f.write(data)
    except Exception as e:
        print("sờ tú pịt")
        print(str(e))
        return False
    return True

def get_data(filename: str) -> str:
    """gets data from file throws exception if not present"""
    file_path = "data/" + filename
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            return data
    except Exception as e:
        error = "Error!"
        return error
    
if __name__ == "__main__":
    get_file_result = get_data("hello.txt")
    print(get_file_result)
    success = store_data("hello.txt", "hi there!")
    if success:
        print("hú hú")
    else:
        print("ops")
