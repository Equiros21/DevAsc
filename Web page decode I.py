# Decode A Web Page challenge at https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

from bs4 import BeautifulSoup
import requests
import re


def decode(url=requests.get("http://nytimes.com")):
    html = url.text.encode()
    webparser = BeautifulSoup(html, features="html.parser")
    headlines = webparser.find_all('h2')
    for x in headlines:
        print('--------------------------------------------------------------------------------\n' + x.get_text())
    print('-----------------------------------------------------------------------------------')


decode()
