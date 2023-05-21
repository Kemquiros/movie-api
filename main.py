from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router
from routers.home import home_router


app = FastAPI()

app.title = "Test API"
app.version = "1.0.0"
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)
app.include_router(home_router)

Base.metadata.create_all(bind=engine)
