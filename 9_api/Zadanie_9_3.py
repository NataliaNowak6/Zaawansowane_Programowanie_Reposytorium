from fastapi import FastAPI
from fastapi.responses import JSONResponse
import csv
from pathlib import Path

app = FastAPI()

# ---------------- MODELE ----------------
class Movie:
    def __init__(self, movieId: str, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId: str, movieId: str, rating: str):
        self.userId = userId
        self.movieId = movieId
        self.rating = float(rating)


class Tag:
    def __init__(self, userId: str, movieId: str, tag: str):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag

# ---------------- FUNKCJE ----------------
def load_csv(csv_path: str, cls) -> list:
    items = []
    path = Path(csv_path)
    if not path.exists():
        return items

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # dynamiczne mapowanie: dopasowuje kolumny CSV do konstruktora
            filtered_row = {k: v for k, v in row.items() if k in cls.__init__.__code__.co_varnames}
            item = cls(**filtered_row)
            items.append(item)
    return items

# ---------------- ENDPOINTY ----------------
@app.get("/movies")
def get_movies():
    movies = load_csv("Bazy_danych/movies.csv", Movie)
    return JSONResponse(content=[m.__dict__ for m in movies])


@app.get("/links")
def get_links():
    links = load_csv("Bazy_danych/links.csv", Link)
    return JSONResponse(content=[l.__dict__ for l in links])


@app.get("/ratings")
def get_ratings():
    ratings = load_csv("Bazy_danych/ratings.csv", Rating)
    return JSONResponse(content=[r.__dict__ for r in ratings])


@app.get("/tags")
def get_tags():
    tags = load_csv("Bazy_danych/tags.csv", Tag)
    return JSONResponse(content=[t.__dict__ for t in tags])