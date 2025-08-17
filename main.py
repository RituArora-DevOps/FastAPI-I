from fastapi import FastAPI, HTTPException, Path, Query
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithId
from typing import Annotated

app = FastAPI()

BANDS = [
    {'id': 1, 'name': 'abc', 'genre': 'Rock'},
    {'id': 2, 'name': 'def', 'genre': 'Hip-Hop'},
    {'id': 3, 'name': 'ghi', 'genre': 'Classic', 'album': [{
        'title': 'abc', 'release_date': '1971-07-21'}]},
    ]

@app.get('/bands')
async def bands(genre: GenreURLChoices | None = None,
                q: Annotated[str | None, Query(max_length=10)]=None,
                # has_albums: bool = False
                ) -> list[BandWithId]:    # here = None means we are defaulting the query parameter to Null  
    band_list = [BandWithId(**b) for b in BANDS]
    if genre:
        band_list = [
                b for b in band_list if b.genre.value.lower() == genre.value
            ]
    if q:
        band_list = [
                b for b in band_list if q.lower() in b.name.lower()
            ]
    
    # if has_albums:
    #     band_list = [b for b in band_list if len(b.albums) > 0]

    return band_list

@app.get('/bands/{band_id}', status_code=206)   
async def band(band_id: Annotated[int, Path(title='The band id')])-> BandWithId:  
    band = next((BandWithId(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail='band not found')
    return band


@app.post("/bands")
async def create_band(band_data: BandCreate) -> BandWithId:
    id = BANDS[-1]['id'] + 1
    band = BandWithId(id=id,  **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band