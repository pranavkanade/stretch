# class=challenge-body-html
# https://www.hackerrank.com/challenges/py-hello-world/problem
from bs4 import BeautifulSoup
import urllib.request
import json

class UrlBuilder():
    def __init__(self, input_json_file):
        self.level = None
        self.input_json_file = input_json_file
        self.slug_object = None
        with open(self.input_json_file, 'r') as json_input:
            self.slug_object = json.load(json_input)

    def get_url_list(self, level=easy):
        self.level = level


