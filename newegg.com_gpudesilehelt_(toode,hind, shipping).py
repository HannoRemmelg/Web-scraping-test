from urllib.request import urlopen
from bs4 import BeautifulSoup as BSoup

target_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
uClient = urlopen(target_url)
page_raw_html = uClient.read()
uClient.close()

page_soup = BSoup(page_raw_html, "html.parser")
containers = page_soup.findAll("div", {"class": "item-container"})

filename = "products.csv"
f = open(filename, "W")

headers = "brand, product_name, shipping"
f.write(headers)

for container in containers:
    #brand = container.div.div.a.img["title"]
    brand_container = container.findAll("a", {"class": "item-brand"})
    product_brand = brand_container[0].img["alt"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    price_ship = container.findAll("li", {"class": "price-ship"})
    product_shipping = price_ship[0].text.strip()

    print("brand: ", product_brand)
    print("product_name: ", product_name)
    print("product_shipping: ", product_shipping)

    f.write(product_brand + "," + product_name.replace(",", "|") + "," + product_shipping + "\n")
