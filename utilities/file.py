import os

class File():
    def __init__(self):
        pass

    def read_file(self, filename):
        if os.path.isfile(filename) is False:
            return TypeError()
        
        with open(filename, 'r') as file_obj:
            file_content = file_obj.read()
        # return the string
        return file_content