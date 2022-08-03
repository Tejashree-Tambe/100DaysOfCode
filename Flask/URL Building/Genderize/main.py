from datetime import date
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    today = date.today()
    year = today.year
    return render_template("index.html", current_year=year)


@app.route('/guess/<name>')
def guess(name):
    gender_response = requests.get(url=f"https://api.genderize.io/?name={name}")
    gender_response.raise_for_status()

    data = gender_response.json()
    name = data["name"]
    gender = data["gender"]

    age_response = requests.get(url=f"https://api.agify.io/?name={name}")
    age_response.raise_for_status()

    data = age_response.json()
    age = data["age"]

    return render_template("genderize.html", name=name, gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)


