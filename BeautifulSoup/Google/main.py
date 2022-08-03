import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.google.com/search?q=javascript")
data = response.text

soup = BeautifulSoup(data, "html.parser")
print(soup.find_all(name="cite", class_="iUh30 Zu0yb qLRx3b tjvcx"))


# site_links = [for tag in]