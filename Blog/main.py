from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/ef931ebdc5cf1d250e0f"
response = requests.get(blog_url)
all_posts = response.json()

app = Flask(__name__, static_url_path='')


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for post in all_posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", requested_post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
