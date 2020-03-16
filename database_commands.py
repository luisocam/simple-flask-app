from flask_site import db
from flask_site.models import Movie

db.drop_all()
db.create_all()

movie_list = [
    {'title': 'Shawshank Redemption, The', 'year':1994, 'rating':9.2},
    {'title': 'Godfather, The', 'year':1972, 'rating':9.1},
    {'title': 'Godfather: Part II, The', 'year':1974, 'rating':9},
    {'title': 'Dark Knight, The', 'year':2008, 'rating':9},
    {'title': '12 Angry Men', 'year':1957, 'rating':8.9},
    {'title': 'Schindler\'s List', 'year':1993, 'rating':8.9},
    {'title': 'Lord of the Rings: The Return of the King, The', 'year':2003, 'rating':8.9},
    {'title': 'Pulp Fiction', 'year':1994, 'rating':8.9},
    {'title': 'Buono, il brutto, il cattivo., Il', 'year':1966, 'rating':8.8},
    {'title': 'Lord of the Rings: The Fellowship of the Ring, The', 'year':2001, 'rating':8.8},
    {'title': 'Fight Club', 'year':1999, 'rating':8.8},
    {'title': 'Forrest Gump', 'year':1994, 'rating':8.8},
    {'title': 'Inception', 'year':2010, 'rating':8.7},
    {'title': 'Star Wars: Episode V - The Empire Strikes Back', 'year':1980, 'rating':8.7},
    {'title': 'Lord of the Rings: The Two Towers, The', 'year':2002, 'rating':8.7}
]



for movie in movie_list:
    
    db.session.add(Movie(title=movie['title'], year=movie['year'], rating=movie['rating']))
    # print(movie['title'], movie ['year'], movie['rating'])

db.session.commit()
print(Movie.query.all())