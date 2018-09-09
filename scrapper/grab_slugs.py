import urllib.request, urllib.parse
import json

'''
PURPOSE : This script can be used to collect slug files
'''

DEST_DATA_DIR = './data/slug/'

def grab_json(difficulty, addon=50):
    offset = 0
    output_file_prefix=difficulty+'_'
    total_number_of_models_fetched = 0
    while True:
        URL = "https://www.hackerrank.com/rest/contests/master/tracks/python/challenges?offset="+str(offset)+"&limit=50&filters%5Bdifficulty%5D%5B%5D="+(difficulty)+"&track_login=true"

        offset += addon
        json_string = urllib.request.urlopen(URL).read()

        json_obj = json.loads(json_string.decode())

        num_of_models_fetched = len(json_obj["models"])
        if num_of_models_fetched > 0:
            total_number_of_models_fetched += num_of_models_fetched
            output_file_name = output_file_prefix+str(offset//addon)+'.json'
            json_data_file = DEST_DATA_DIR + output_file_name
            with open(json_data_file, 'w') as out_file:
                out_file.write(json_string.decode())
        else:
            print(difficulty, " done")
            print("total models : ", total_number_of_models_fetched)
            break

def grab_easy_slugs():
    grab_json("easy", addon=50)

def grab_medium_slugs():
    grab_json("medium", addon=50)

def grab_hard_slugs():
    grab_json("hard")

if __name__ == "__main__":
    grab_easy_slugs()
    grab_medium_slugs()
    grab_hard_slugs()