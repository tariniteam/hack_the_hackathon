import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

class ConnectToGithub():

    def __init__(self, url):
        self.url = url

    def get_sql_scripts(self):

        return sql_scripts

if __name__ == "__main__":
    url = 'https://github.com/tariniteam/hack_the_hackathon/tree/main/Query%20Metadata%20Parser/SQL%20Scripts'
    objConnectToGithub = ConnectToGithub(url)
    sql_scripts = objConnectToGithub.get_sql_keyword_list()



#with open("myfile.csv", "w") as f:
 #   f.write(resp.text)