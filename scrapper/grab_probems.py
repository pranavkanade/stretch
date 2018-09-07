# class=challenge-body-html
from url_builder import UrlBuilder
from bs4 import BeautifulSoup
import urllib.request
import re

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
        new_text.append(BeautifulSoup(each_line, 'html.parser').text)

    with open('./data/problems/'+level+'/'+slug+'.txt', 'w') as grabbed_prob:
        grabbed_prob.write(url)
        grabbed_prob.write("\n\n")
        grabbed_prob.writelines(new_text)
        grabbed_prob.write("\n\n")
        grabbed_prob.writelines([each_line.text for each_line in difficulty_block])

urlbuilder = UrlBuilder('./data/slugs_with_levels.json')
levels = ["Easy", "Hard", "Medium"]

# for level in levels: use last one
url_dict = urlbuilder.get_url_list(level="Hard")

for slug in url_dict.keys():
    grab_problems(slug, url_dict[slug], "Hard")
# grab_problems('py-hello-world', 'https://www.hackerrank.com/challenges/py-hello-world/problem')
