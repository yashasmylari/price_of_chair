import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-partners-easy-care-200-thread-count-polycotton-bedding/white/p5071125")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class":"price price--large" })
string_price = element.text.strip()
price_without = string_price[1:5]
price_without_pound = float(price_without)

if price_without_pound < 100:
    print("you can buy the chair")
    print("current price of the chair is {}".format(string_price))
else:
    print("Its too expensive")