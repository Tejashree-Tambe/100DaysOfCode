from flask import Flask, render_template, request
import requests
import smtplib

blog_url = "https://api.npoint.io/ef931ebdc5cf1d250e0f"
response = requests.get(blog_url)
all_posts = response.json()

MY_EMAIL = "pythondeveloper0401@gmail.com"
PASSWORD = "Python123"
SUBJECT = "Blog Contact"

app = Flask(__name__, static_url_path='')

# config file has STATIC_FOLDER='/core/static'
app.static_url_path = app.config.get('STATIC_FOLDER')

# set the absolute path to the static folder
app.static_folder = app.root_path + app.static_url_path

print(app.static_url_path)
print(app.static_folder)


@app.route('/')
def home():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        print(f"{name}\n{email}\n{phone}\n{message}")
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:{SUBJECT}\n\n{message}")

        return render_template("contact.html", message=message)

    else:
        return render_template("contact.html")


@app.route('/post/<int:post_id>')
def post(post_id):
    requested_post = None
    for post in all_posts:
        if post["id"] == post_id:
            requested_post = post
    return render_template("post.html", requested_post=requested_post)


# @app.route('/form_entry', methods=['POST'])
# def receive_data():
#     name = request.form['name']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#
#     print(f"{name}\n{email}\n{phone}\n{message}")
#     return '<h1>Successfully sent your message!</h1>'


if __name__ == "__main__":
    app.run(debug=True)
