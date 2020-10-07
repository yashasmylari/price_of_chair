import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.de/-/en/gp/product/B07T83CDRD?pf_rd_r=SH6MM453EPBHH0ZNSNVV&pf_rd_p=f6634045-2cd8-4654-8338-b9246a89c6f1")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id":"priceblock_saleprice", "class":"a-size-medium a-color-price priceBlockSalePriceString" })
print(element.text)

#<span id="priceblock_saleprice" class="a-size-medium a-color-price priceBlockSalePriceString">€24.99</span>