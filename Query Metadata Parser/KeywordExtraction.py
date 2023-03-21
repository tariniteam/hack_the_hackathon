import requests
from bs4 import BeautifulSoup
import pandas as pd

class KeyWordExtraction():

    def __init__(self, url):
        self.url = url
    def get_json_data(self):
        print("url is", self.url)
        html_response = requests.get(url=self.url)
        html_data = html_response.text
        print(html_response)
        print (html_data)
        soup = BeautifulSoup(html_data, 'html.parser')
        print(soup)
        text = ''
        print ('Extracted Text')
        for data in soup.find_all("p"):
            print(data.get_text())


if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_SQL_reserved_words'
    objKeyWordExtraction = KeyWordExtraction (url)
    objKeyWordExtraction.get_json_data()
