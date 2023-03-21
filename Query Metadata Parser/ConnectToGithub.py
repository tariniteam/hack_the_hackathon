import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

class ConnectToGithub():

    def __init__(self, base_github_folder):
        self.base_github_folder = base_github_folder

    def get_sql_scripts(self):
        print (self.base_github_folder)

    def read_sql_scripts(self):
        html_response = requests.get(url=self.url)
        html_data = html_response.text
        soup = BeautifulSoup(html_data, 'html.parser')
        print('SQL Scripts')
        table = soup.find_all('table')
        df = pd.read_html(str(table))[0]
        print(df)
        sql_scripts = df.iloc[:, 1].tolist()
        return sql_scripts

if __name__ == "__main__":
    base_github_folder = 'https://github.com/tariniteam/hack_the_hackathon/tree/main/Query%20Metadata%20Parser/SQL%20Scripts'
    url = 'https://github.com/tariniteam/hack_the_hackathon/blob/main/Query%20Metadata%20Parser/SQL%20Scripts/SQL%20Script%201.sql'
    objConnectToGithub = ConnectToGithub(base_github_folder)
    sql_scripts = objConnectToGithub.read_sql_scripts()
    print (sql_scripts)


