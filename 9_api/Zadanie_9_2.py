from fastapi import FastAPI
from fastapi.responses import JSONResponse
import csv
from pathlib import Path

app = FastAPI()

class Movie:
    def __init__(self, id: str, title: str, genres: str):
        self.id = id
        self.title = title
        self.genres = genres

def load_movies_from_csv(csv_path: str) -> list[Movie]:
    movies = []
    path = Path(csv_path)
    if not path.exists():
        return movies

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = Movie(
                id=row["movieId"],
                title=row["title"],
                genres=row["genres"],
            )
            movies.append(movie)
    return movies

@app.get("/movies")
def get_movies():
    movies = load_movies_from_csv("Bazy_danych/movies.csv")
    return JSONResponse(content=[movie.__dict__ for movie in movies])