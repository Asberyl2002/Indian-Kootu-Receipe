from fastapi import FastAPI
from enum import Enum

class itemid(str, Enum):
    cabbagekootu = "cabbagekootu"
    greenchilli = "greenchilli"
    curryleaves = "curryleaves"
    onion = "onion"


app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/indian_kootu_receipe/{item_id}")
async def read_item(item_id: str, q: str | None = None):

    if q == "yes":
        return {"message": f"{item_id} is Cleaned"}

    return {"message": f"{item_id} is not cleaned"}