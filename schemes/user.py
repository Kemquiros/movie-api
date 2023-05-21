from pydantic import BaseModel, Field


class User(BaseModel):
    email: str = Field(min_length=5, max_length=25)
    password: str = Field(min_length=6, max_length=20)
