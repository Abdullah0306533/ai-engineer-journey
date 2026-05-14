from fastapi import FastAPI
app = FastAPI()

@app.get("/crops/{crop_name}")
def crop(crop_name: str):
    return {"crop_name": crop_name}

@app.get("/search")
def search(crop_name: str, disease:str=None,):
    return {"Searching for": crop_name,"Crop Disease":disease}



