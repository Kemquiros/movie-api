from models.movie import Movie as MovieModel
from schemes.movie import Movie


class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie_by_id(self, id: int):
        result = self.db.query(MovieModel).filter(
            MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category: str):
        result = self.db.query(MovieModel).filter(
            MovieModel.category == category).all()
        return result

    def create_movie(self, movie: Movie):
        new_movie = MovieModel(**movie.dict())
        self.db.add(new_movie)
        self.db.commit()
        return new_movie

    def update_movie(self, movie: Movie, id_movie: int):
        movie_result = self.db.query(MovieModel).filter(
            MovieModel.id == id_movie).first()
        if not movie_result:
            return movie_result
        movie_result.title = movie.title
        movie_result.overview = movie.overview
        movie_result.year = movie.year
        movie_result.rating = movie.rating
        movie_result.category = movie.category
        self.db.commit()
        return movie_result

    def delete_movie(self, movie: Movie):
        self.db.delete(movie)
        self.db.commit()
