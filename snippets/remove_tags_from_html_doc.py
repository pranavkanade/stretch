from bs4 import BeautifulSoup

file = './new_html.txt'

with open(file, 'r') as finp:
    html = finp.read()
    soup = BeautifulSoup(html, 'html.parser')
    # soup.span.decompose()
    # text = soup.findAll(['p', 'pre'])
    with open('./test_res.txt', 'w') as fout:
        fout.write(soup.text)