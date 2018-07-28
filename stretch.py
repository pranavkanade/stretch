from utilities.file import File
import os
from pprint import pprint

# Path to data dir
DATA_DIR = './data'

def main():
    file_obj = File()
    problemset_filename = 'problem_set1.txt'
    data = file_obj.read_file(os.path.join(DATA_DIR, problemset_filename))
    # print all the data in a list format line by line.
    pprint([line for line in data.strip('\n').split('\n')])

if __name__ == '__main__':
    main()