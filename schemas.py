from datetime import date
from enum import Enum
from pydantic import BaseModel, validator

class GenreURLChoices(Enum):
    ROCK = 'rock'
    HIP_HOP = 'hip-hop'
    CLASSIC = 'classic' 

class GenreChoices(Enum):
    ROCK = 'Rock'
    HIP_HOP = 'Hip-Hop'
    CLASSIC = 'Classic' 


class Album(BaseModel):
    title: str
    release_date: date

class BandBase(BaseModel):
    #{'id': 1, 'name': 'abc', 'genre': 'Rock'}
    #id: int
    name: str
    genre: GenreChoices
    albums: list[Album] = [] # default to empty list

class BandCreate(BandBase):
     @validator('genre', pre=True)
     def title_case_genre(cls, value):
         return value.title()

class BandWithId(BandBase):
    id:int