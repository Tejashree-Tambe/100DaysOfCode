from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# all_a_tags = soup.find_all(name="a")
#
# for a_tag in all_a_tags:
#     print(a_tag.getText())
#     print(a_tag.get("href"))

# print(soup.find(name="h1", id="name"))
# print(soup.find(name="h3", class_="heading"))
# print(soup.select_one(selector="p a"))
# print(soup.select_one("#name"))
# print(soup.select(".heading"))



