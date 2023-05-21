from fastapi import APIRouter
from fastapi.responses import JSONResponse
from jwt_manager import create_token
from schemes.user import User


user_router = APIRouter()


@user_router.post(
    '/login',
    tags=['auth'],
    response_model=dict)
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin123":
        token: str = create_token(user.dict())
        return JSONResponse(
            content=token,
            status_code=200
        )
    return JSONResponse(
        content=[],
        status_code=200
    )
