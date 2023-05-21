from fastapi import APIRouter, Path, Query, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from middlewares.jwt_bearer import JWTBearer
from models.movie import Movie as MovieModel
from config.database import Session
from services.movie import MovieService
from schemes.movie import Movie


movie_router = APIRouter()


@movie_router.get(
    '/movies',
    tags=['movies'],
    response_model=List[Movie],
    status_code=200,
    dependencies=[Depends(JWTBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get(
    '/movies/{movie_id}',
    tags=['movies'],
    response_model=Movie,
    status_code=200)
def get_movie(movie_id: int = Path(ge=1, le=2000)) -> Movie:
    db = Session()
    movie = MovieService(db).get_movie_by_id(movie_id)
    if not movie:
        return JSONResponse(status_code=404, content={
            "message": "La película no existe",
            "id": movie_id
        })
    return JSONResponse(content=jsonable_encoder(movie))


@movie_router.get(
    '/movies/',
    tags=['movies'],
    response_model=List[Movie])
def get_movie_by_category(
        query_category: str = Query(min_length=2, max_length=20)) -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies_by_category(query_category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


""" @movie_router.post(
    '/movies/v1',
    tags=['movies'],
    response_model=dict,
    status_code=201)
def create_movie(
        title: str = Body(),
        overview: str = Body(),
        year: str = Body(),
        rating: float = Body(),
        category: str = Body()) -> dict:
    movie = {
        'id': len(movies)+1,
        'title': title,
        'overview': overview,
        'year': year,
        'rating': rating,
        'category': category
    }
    movies.append(movie)
    return JSONResponse(status_code=201, content={
        "message": "Se ha registrado la película",
        "id": movie['id']
    }) """


@movie_router.post(
    '/movies/v2',
    tags=['movies'],
    response_model=dict,
    status_code=201)
def create_movie_2(movie: Movie) -> dict:
    db = Session()
    new_movie = MovieService(db).create_movie(movie)
    return JSONResponse(status_code=201, content={
        "message": "Se ha registrado la película",
        "id": new_movie.id
    })


@movie_router.put(
    '/movies/{id_movie}',
    tags=['movies'],
    response_model=dict,
    status_code=200)
def update_movie(movie: Movie, id_movie: int) -> dict:
    db = Session()
    movie_result = MovieService(db).get_movie_by_id(id_movie)
    if not movie_result:
        return JSONResponse(status_code=404, content={
            "message": "La película no existe",
            "id": id_movie
        })
    movie_result = MovieService(db).update_movie(movie, id_movie)
    return JSONResponse(status_code=200, content={
        "message": "Se ha actualizado la película",
        "movie": jsonable_encoder(movie_result)
    })


@movie_router.delete(
    '/movies/{id_movie}',
    tags=['movies'],
    response_model=dict,
    status_code=200)
def delete_movie(id_movie: int) -> dict:
    db = Session()
    movie = MovieService(db).get_movie_by_id(id_movie)
    if not movie:
        return JSONResponse(status_code=404, content={
            "message": "La película no existe",
            "id": id_movie
        })
    MovieService(db).delete_movie(movie)
    return JSONResponse(status_code=200, content={
        "message": "Se ha eliminado la película",
        "id": id_movie
    })
