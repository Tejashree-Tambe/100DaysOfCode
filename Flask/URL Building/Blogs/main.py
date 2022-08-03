
from datetime import date
from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
data = response.json()
print(data)

for blog in data:
    print(blog)



