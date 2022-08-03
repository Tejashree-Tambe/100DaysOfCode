from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(
    "https://www.zillow.com/homes/San-Francisco,-CA_rb/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55177535009766%2C%22east%22%3A-122.31488264990234%2C%22south%22%3A37.69926912019228%2C%22north%22%3A37.851235694487485%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D",
    headers=header)
zillow_html = response.text

soup = BeautifulSoup(zillow_html, "html.parser")

# Get prices
property_prices = soup.find_all(name="div", class_="list-card-price")
prices = []
for price in property_prices:
    price_text = price.getText()
    if '/' in price_text:
        prices.append(price_text.split('/')[0])
    else:
        prices.append(price_text.split('+')[0])

# Get links
property_links = soup.select(".list-card-top a")
links = []
for property_link in property_links:
    link = property_link["href"]
    if "http" not in link:
        links.append(f"https://www.zillow.com{link}")
    else:
        links.append(link)

# Get address
property_addresses = soup.find_all(class_="list-card-addr")
addresses = []

for property_address in property_addresses:
    address = property_address.getText()
    addresses.append(address.split('|')[-1])

no_of_properties = len(addresses)

print("Got all data of the property\nOpening Chrome Browser")

# To fill form
chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

for i in range(no_of_properties):
    google_form_link = "https://forms.gle/ieC5srQgbraPaPPJ8"
    driver.get(google_form_link)

    time.sleep(3)

    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.click()
    address.send_keys(addresses[i])

    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.click()
    price.send_keys(prices[i])

    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.click()
    link.send_keys(links[i])

    submit_button = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    submit_button.click()
