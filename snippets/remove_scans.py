import re

file = './data/problems/Hard/maximize-it.txt'

with open(file, 'r') as finp:
    html = finp.read()

    (html, n) = re.subn("(<span .*?</span>)", " TOK ", html)

    with open('new_html.txt', 'w') as fout:
        fout.write(html)