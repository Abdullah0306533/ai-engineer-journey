from fastapi import FastAPI,File,UploadFile

app = FastAPI()
@app.post("/upload_files")
async def upload_files(file: UploadFile):
    return {"filename": file.filename,"file size":file.size,"content_type":file.content_type}
