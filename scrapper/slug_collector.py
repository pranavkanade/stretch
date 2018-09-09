import json
import os
from pprint import pprint

INPUT_SLUG_DATA_DIR = './data/slug/'
OUTPUT_SLUG_DATA_DIR = './data/'
OUTPUT_SLUG_FILE = 'slugs_with_levels.json'

def get_slug_file_paths(slug_data_dir):
    return [os.path.join(slug_data_dir, file)
            for file in os.listdir(slug_data_dir)]

def collect_slugs(slug_files_list):
    slug_dict = dict()
    for each_data_file in slug_files_list:
        # build a json object
        with open(each_data_file, 'r') as json_data_file:
            data_obj = json.load(json_data_file)
            for each_model in data_obj["models"]:
                slug_dict[each_model["slug"]] = {
                    "name" : each_model["name"],
                    "level" : each_model["difficulty_name"]
                }
    return slug_dict

def write_collected_slugs(slug_dict, slug_data_dir):
    output_slug_file = os.path.join(slug_data_dir, OUTPUT_SLUG_FILE)

    with open(output_slug_file, 'w') as json_slug_file:
        json.dump(slug_dict, json_slug_file)

    print("done writing slugs & names")
    print(len(slug_dict.keys()))

def main():
    slug_data_dir = INPUT_SLUG_DATA_DIR
    slug_data_dir = os.path.abspath(slug_data_dir)
    slug_files_list = get_slug_file_paths(slug_data_dir)
    slug_dict = collect_slugs(slug_files_list)

    # find output dir
    slug_data_dir = OUTPUT_SLUG_DATA_DIR
    slug_data_dir = os.path.abspath(slug_data_dir)
    write_collected_slugs(slug_dict, slug_data_dir)
    # pprint(slug_dir_contents)

if __name__ == '__main__':
    main()