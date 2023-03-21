import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

class ConnectToGithub():

    def __init__(self, url):
        self.url = url

    def get_sql_keyword_list(self):
       
        return keyword_list

if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/List_of_SQL_reserved_words'
    objConnectToGithub = ConnectToGithub(url)
    keyword_list = objConnectToGithub.get_sql_keyword_list()

