from datetime import date
from enum import Enum
from pydantic import BaseModel, validator
from sqlmodel import SQLModel, Field

class GenreURLChoices(Enum):
    ROCK = 'rock'
    HIP_HOP = 'hip-hop'
    CLASSIC = 'classic' 

class GenreChoices(Enum):
    ROCK = 'Rock'
    HIP_HOP = 'Hip-Hop'
    CLASSIC = 'Classic' 


class AlbumBase(SQLModel):
    title: str
    release_date: date

class Album(AlbumBase, table = True):
    id: int = Field(default=None, primary_key=True)

class BandBase(SQLModel):
    #{'id': 1, 'name': 'abc', 'genre': 'Rock'}
    #id: int
    name: str
    genre: GenreChoices
    

class BandCreate(BandBase):
     albums: list[AlbumBase] | None = None # default to empty list

     @validator('genre', pre=True)
     def title_case_genre(cls, value):
         return value.title()

class BandWithId(BandBase):
    id:int