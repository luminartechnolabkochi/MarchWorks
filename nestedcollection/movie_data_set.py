movies=[
  {
    "id": "tt0094721",
    "title": "Beetlejuice",
    "language": "en",
    "year": 1988,
    "runtime": 92,
    "genres": ["Comedy", "Fantasy"],
    "rating": 7.5
  },
  {
    "id": "tt0087089",
    "title": "The Cotton Club",
    "language": "en",
    "year": 1984,
    "runtime": 127,
    "genres": ["Crime", "Drama", "Music"],
    "rating": 6.5
  },
  {
    "id": "tt0093773",
    "title": "The Big Blue",
    "language": "fr",
    "year": 1988,
    "runtime": 132,
    "genres": ["Adventure", "Drama", "Romance"],
    "rating": 7.6
  },
  {
    "id": "tt0097165",
    "title": "Dead Poets Society",
    "language": "en",
    "year": 1989,
    "runtime": 128,
    "genres": ["Comedy", "Drama"],
    "rating": 8.1
  },
  {
    "id": "tt0096256",
    "title": "Rain Man",
    "language": "en",
    "year": 1988,
    "runtime": 133,
    "genres": ["Drama"],
    "rating": 8.0
  },
  {
    "id": "tt0095016",
    "title": "Die Hard",
    "language": "en",
    "year": 1988,
    "runtime": 132,
    "genres": ["Action", "Thriller"],
    "rating": 8.2
  },
  {
    "id": "tt0095327",
    "title": "Grave of the Fireflies",
    "language": "ja",
    "year": 1988,
    "runtime": 89,
    "genres": ["Animation", "Drama", "War"],
    "rating": 8.5
  },
  {
    "id": "tt0097576",
    "title": "Indiana Jones and the Last Crusade",
    "language": "en",
    "year": 1989,
    "runtime": 127,
    "genres": ["Action", "Adventure"],
    "rating": 8.2
  },
  {
    "id": "tt0099348",
    "title": "Dances with Wolves",
    "language": "en",
    "year": 1990,
    "runtime": 181,
    "genres": ["Adventure", "Drama", "Western"],
    "rating": 8.0
  },
  {
    "id": "tt0099685",
    "title": "Goodfellas",
    "language": "en",
    "year": 1990,
    "runtime": 146,
    "genres": ["Biography", "Crime", "Drama"],
    "rating": 8.7
  },
  {
    "id": "tt0102926",
    "title": "The Silence of the Lambs",
    "language": "en",
    "year": 1991,
    "runtime": 118,
    "genres": ["Crime", "Drama", "Thriller"],
    "rating": 8.6
  },
  {
    "id": "tt0103064",
    "title": "Terminator 2: Judgment Day",
    "language": "en",
    "year": 1991,
    "runtime": 137,
    "genres": ["Action", "Sci-Fi"],
    "rating": 8.6
  },
  {
    "id": "tt0105236",
    "title": "Reservoir Dogs",
    "language": "en",
    "year": 1992,
    "runtime": 99,
    "genres": ["Crime", "Drama", "Thriller"],
    "rating": 8.3
  },
  {
    "id": "tt0108052",
    "title": "Schindler's List",
    "language": "en",
    "year": 1993,
    "runtime": 195,
    "genres": ["Biography", "Drama", "History"],
    "rating": 9.0
  },
  {
    "id": "tt0110912",
    "title": "Pulp Fiction",
    "language": "en",
    "year": 1994,
    "runtime": 154,
    "genres": ["Crime", "Drama"],
    "rating": 8.9
  },
  {
    "id": "tt0111161",
    "title": "The Shawshank Redemption",
    "language": "en",
    "year": 1994,
    "runtime": 142,
    "genres": ["Drama"],
    "rating": 9.3
  },
  {
    "id": "tt0110413",
    "title": "Léon: The Professional",
    "language": "fr",
    "year": 1994,
    "runtime": 110,
    "genres": ["Action", "Crime", "Drama"],
    "rating": 8.5
  },
  {
    "id": "tt0114369",
    "title": "Se7en",
    "language": "en",
    "year": 1995,
    "runtime": 127,
    "genres": ["Crime", "Drama", "Mystery"],
    "rating": 8.6
  },
  {
    "id": "tt0114709",
    "title": "Toy Story",
    "language": "en",
    "year": 1995,
    "runtime": 81,
    "genres": ["Animation", "Adventure", "Comedy"],
    "rating": 8.3
  },
  {
    "id": "tt0118799",
    "title": "Life Is Beautiful",
    "language": "it",
    "year": 1997,
    "runtime": 116,
    "genres": ["Comedy", "Drama", "Romance"],
    "rating": 8.6
  }
]

#q1 total number of movies

# print(len(movies))

#q2 display english movies names

english_movie_names=[m.get("title") for m in movies if m.get("language")=="en" ]

# print(english_movie_names)

#q3 display Toy Story movie detail
movie_detail=[m for m in movies if m.get("title")=="Life Is Beautiful"]
# print(movie_detail)

#q4 movies with rating above > 8.5

rating_filter=[m.get("title") for m in movies if m.get("rating") > 8.5]
# print(rating_filter)


#q5 comdey movies

comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres")]

# print(comedy_movies)

#q6 movie with highest running time

def get_movie_run_time(dictionary):

    return dictionary.get("runtime")

longest_movie=max(movies,key=get_movie_run_time)

# print(longest_movie)


#q7 movies released in 1997

year_filter=[m.get("title") for m in movies if m.get("year") == 1997]
# print(year_filter)

#q9 year with most number of movies released

years_list=[m.get("year") for m in movies]
yc={}

for y in years_list:

    if y in yc:

        yc[y]+=1

    else:

        yc[y]=1

# print(yc)
# q10 in which genre most numbers movies


all_genres=[g for m in movies for g in m.get("genres")]

gc={}

for g in all_genres:

    if g in gc:

        gc[g]+=1

    else:

        gc[g]=1
print(gc)
#q11 languages

#q12 top rated movie

