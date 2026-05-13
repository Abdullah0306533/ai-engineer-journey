from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name_crop:str


app = FastAPI()


@app.get("/first_api")
def first_api():
    return {"Hello": "My First API"}

@app.post("/detect")
def detect(crop_name: Item):
    return {"Crop": crop_name.name_crop,"status":"analyzing"}