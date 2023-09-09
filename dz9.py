import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find_all("td", {"data-label": "Офіційний курс"})

    print("1 Долар США коштуе " + price[7].text + " гривень")
    print("1 Євро коштуе " + price[8].text + " гривень")
else:
    print("Cannot connect to the server! Error " + str(response.status_code))