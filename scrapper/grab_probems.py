# class=challenge-body-html
from url_builder import UrlBuilder
from bs4 import BeautifulSoup
import urllib.request
import re
import time
import json

def grab_problems(slug, url, level):
    html_doc = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    challenge_body = soup.find('div', attrs={'class': "challenge-body-html"})
    difficulty_block = soup.find_all('div',
                                     attrs={'class': "difficulty-block"})

    problem_text = challenge_body.findAll(['p', 'pre'])
    problem_text = map(str, problem_text)
    new_text = []
    for each_line in problem_text:
        (each_line, n) = re.subn("(<span .*?</span>)", " TOK ", each_line)
        new_text.append(BeautifulSoup(each_line, 'html.parser').text.encode("utf-8"))
    with open('./data/problems/'+level+'/'+slug+'.txt', 'wb') as grabbed_prob:
        grabbed_prob.write(url.encode("utf-8"))
        grabbed_prob.write("\n\n".encode("utf-8"))
        try:
            grabbed_prob.writelines(new_text)
        except UnicodeEncodeError:
            return False
        grabbed_prob.write("\n\n".encode("utf-8"))
        grabbed_prob.writelines([each_line.text.encode("utf-8") for each_line in difficulty_block])
    return True

urlbuilder = UrlBuilder('./data/slugs_with_levels.json')
levels = ["Easy", "Hard", "Medium"]

error_occured = dict()

for level in levels:
    url_dict = urlbuilder.get_url_list(level=level)
    error_occured[level] = []
    for slug in url_dict.keys():
        ret_val = grab_problems(slug, url_dict[slug], level)
        if ret_val is False:
            error_occured[level].append(slug)
        time.sleep(0.5)

with open('./data/problems/didnot_get.json', 'w') as errfile:
    json.dump(error_occured, errfile)
# grab_problems('py-hello-world', 'https://www.hackerrank.com/challenges/py-hello-world/problem')
