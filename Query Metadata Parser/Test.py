import requests

url = "https://github.com/tariniteam/hack_the_hackathon/blob/main/Query%20Metadata%20Parser/SQL%20Scripts/SQL%20Script%201.sql"
resp = requests.get(url)
with open("C:/Users/harsha/OneDrive/Desktop/HARSHA DATA/Cloned Repo/Projects/Query Metadata Parser/myfile.sql", "w", encoding="utf-8") as f:
    f.write(resp.text)