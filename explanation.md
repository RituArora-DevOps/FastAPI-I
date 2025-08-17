@app.get('/bands/{band_id}', status_code=206)   # FastAPI route decorator - whenever someone makes a GET request call the function band
# {band_id} is a path parameter
# 206 -for successful but partial response
async def band(band_id: int)-> BandWithId:   # async function that runs concurrently (for non-blocking requests)
    # (band_id: int) - FastAPI automatically validates that the path parameter must be an integer
    # declares the function returns a dictionary
    band = next((BandWithId(**b) for b in BANDS if b['id'] == band_id), None)
    # next(..., none) - returns the first matching band, or None if not found
    # Band(**b) - IT GIVES A BAND MODEL OBJECT RATHER THAN GIVING A DICTIONARY - Band(id=2, name=def, genre=Hip-Hop)
    # Benefits of using Pydantic BaseModel - validates data, ensures type safety, converts into JSON cleanly
    if band is None:
        #status code 404
        raise HTTPException(status_code=404, detail='band not found')
        # HttpException if from fastapi/starlette
        # FastAPI automatically converts this into a proper JSON error response
    return band

# @app.get('/bands/genre/{genre}')
# async def bands_for_genre(genre: GenreURLChoices) -> list[dict]:
#     return [
#         b for b in BANDS if b['genre'].lower() == genre.value
#     ]