from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=False)


db.create_all()


class EditForm(FlaskForm):
    rating = StringField(label='Your Rating Out of 10 e.g 7.5')
    review = StringField(label='Your Review')
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


app.secret_key = "any-string-you-want-just-keep-it-secret"

api_key = "093243b91d7a3d8ad4f2adf7b5a2f06b"
search_api_url = "https://api.themoviedb.org/3/search/movie"
find_api_url = "https://api.themoviedb.org/3/movie"
image_api_url = "https://image.tmdb.org/t/p/w500"


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    
    return render_template("index.html", movies=all_movies)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    movie_id = request.args.get("movie_id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()

    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        title = add_form.title.data
        api_params = {
            "api_key": api_key,
            "query": title
        }

        response = requests.get(search_api_url, params=api_params)
        api_data = response.json()['results']
        return render_template("select.html", options=api_data)

    return render_template("add.html", form=add_form)


@app.route('/find', methods=['POST', 'GET'])
def find_movie():
    movie_id = request.args.get('movie_id')
    if movie_id:
        api_params = {
            "api_key": api_key,
            "language": "en-US"
        }
        response = requests.get(url=f"{find_api_url}/{movie_id}", params=api_params)
        movie_found = response.json()

        new_movie = Movie(
            title=movie_found['title'],
            description=movie_found['overview'],
            year=movie_found['release_date'].split("-")[0],
            img_url=f"{image_api_url}/{movie_found['poster_path']}",
            # rating=7.9,
            # review="Good Movie",
            # ranking=10
        )
        db.session.add(new_movie)
        print("Hlo")
        db.session.commit()
        print("HI")
        return redirect(url_for("update", movie_id=new_movie.id))


@app.route("/edit", methods=['POST', 'GET'])
def update():
    edit_form = EditForm()
    movie_id = request.args.get("movie_id")
    movie = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        movie.rating = float(edit_form.rating.data)
        movie.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, edit_form=edit_form)


if __name__ == '__main__':
    app.run(debug=True)
