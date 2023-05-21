from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=2, max_length=15)
    overview: str = Field(min_length=5, max_length=50)
    year: int = Field(gt=0, lt=2024)
    rating: float = Field(ge=0.0, le=10.0)
    category: str

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'title': 'Una película',
                'overview': "Con su descripción",
                'year': 2020,
                'rating': 5.0,
                'category': 'Drama'
            }
        }
