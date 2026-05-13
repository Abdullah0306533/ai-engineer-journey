from fastapi import FastAPI, UploadFile, HTTPException

app = FastAPI()
@app.post("/upload_files")
async def upload_files(file: UploadFile):
    if file.content_type not in ["image/jpeg","image/png","image/jpg"] :
        raise HTTPException(status_code=400,detail="Invalid file type")
    return {"filename": file.filename,"file size":file.size,"content_type":file.content_type}
