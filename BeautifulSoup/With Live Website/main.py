import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
yc_html = response.text

soup = BeautifulSoup(yc_html, "html.parser")
article_tags = soup.find_all(name="a", class_="storylink")
# print(article_tags)

article_texts = [tag.getText() for tag in article_tags]
# print(article_texts)

article_links = [tag.get("href") for tag in article_tags]
# print(article_links)

article_upvote = soup.find_all(name="span", class_="score")
article_upvotes = [int(tag.getText().split()[0]) for tag in article_upvote]
print(article_upvotes)

max_upvotes_index = article_upvotes.index(max(article_upvotes))

print(article_texts[max_upvotes_index])
