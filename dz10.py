import requests
from bs4 import BeautifulSoup
import sqlite3

response = requests.get("https://sinoptik.ua")
if response.status_code == 200:
    response = BeautifulSoup(response.text, "html.parser")
    date = response.find_all("p", {"class": "date"})
    month = response.find_all("p", {"class": "month"})
    minTemp = response.find_all("div", {"class": "min"})
    maxTemp = response.find_all("div", {"class": "max"})

    db = sqlite3.connect("db.sl3", 5)
    cur = db.cursor()

    for i in range(7):

        data = [date[i].text + " " + month[i].text, minTemp[i].text, maxTemp[i].text]
        cur.execute("INSERT INTO temp (time, minTemp, maxTemp) VALUES (?, ?, ?)", data)

    # cur.execute("CREATE TABLE temp (time Text, minTemp Text, maxTemp Text);")

    # cur.execute("DELETE FROM temp")

    db.commit()
    db.close()
else:
    print("Cannot connect to the server! Error " + str(response.status_code))
