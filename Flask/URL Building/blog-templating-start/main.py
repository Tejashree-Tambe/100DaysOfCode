from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_blogs = response.json()

app = Flask(__name__, static_url_path='')


@app.route('/')
def home():
    return render_template("index.html", all_blogs=all_blogs)


@app.route('/post/<int:blog_id>')
def show_blog(blog_id):
    requested_blog = None
    for blog in all_blogs:
        # print()
        if blog["id"] == blog_id:
            requested_blog = blog
    return render_template("post.html", requested_blog=requested_blog)


if __name__ == "__main__":
    app.run(debug=True)
