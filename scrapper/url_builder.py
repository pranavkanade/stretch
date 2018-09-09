# This class generates URLs like following
# https://www.hackerrank.com/challenges/py-hello-world/problem
import json
# from pprint import pprint

class UrlBuilder():
    def __init__(self, input_json_file):
        self.level = None
        self.url_prefix = "https://www.hackerrank.com/challenges/"
        self.url_suffix = "/problem"
        self.input_json_file = input_json_file
        self.slug_object = None
        with open(self.input_json_file, 'r') as json_input:
            self.slug_object = json.load(json_input)

    # levels : Easy, Hard, Medium
    def get_url_list(self, level="Easy"):
        self.level = level
        res = []
        return {slug: (self.url_prefix + slug + self.url_suffix)
                for slug in self.slug_object.keys()
                if self.slug_object[slug]["level"] == level}

# if __name__ == "__main__":
#     builder = UrlBuilder('./data/slugs_with_levels.json')
#     slugs_dict = builder.get_url_list(level="Hard")
#     pprint(slugs_dict)