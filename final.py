import sqlite3
from bs4 import BeautifulSoup
import requests

# Парсинг сайту
response = requests.get("https://www.bbc.com/ukrainian/features-66330880")
if response.status_code == 200:
    response = BeautifulSoup(response.text, "html.parser")
    lisT = response.find_all("h2", {"tabindex": "-1"})

    # Робота з БД

    db = sqlite3.connect("database.sl3", 5)
    cur = db.cursor()

    # cur.execute("CREATE TABLE final_table (name Text);")
    # cur.execute("DROP TABLE final_table;")
    cur.execute("DELETE FROM final_table;")

    for i in range(10):
        data = [lisT[i].text]
        # cur.execute("INSERT INTO final_table (name) VALUES (?);", data)

    db.commit()
    db.close()
