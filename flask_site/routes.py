from flask import render_template, url_for
from flask_site import app
from flask_site.models import Movie

@app.route('/')
def home():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)
