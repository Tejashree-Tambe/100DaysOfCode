from bs4 import BeautifulSoup
import requests

EMPIRE_URL = "https://www.timeout.com/newyork/movies/best-movies-of-all-time"
response = requests.get(EMPIRE_URL)
empire_html = response.text

soup = BeautifulSoup(empire_html, "html.parser")

title_tag = soup.find_all(name="h3", class_="_h3_cuogz_1")
titles = [tag.getText() for tag in title_tag]

all_titles = "\n".join(titles)
titles = all_titles.replace(" ", "")

with open("movies_to_watch.txt", "wb") as file:
    file.write(titles.encode("utf-8"))
