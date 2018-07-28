class Error():
    def __init__(self):
        print("An error has occured !")

class TypeError(Error):
    def __init__(self):
        print("This is Type Error\nThere is a type mismatch.. ! Please fix it.")