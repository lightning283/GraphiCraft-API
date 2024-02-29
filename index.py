from fastapi import FastAPI, File, UploadFile
import shutil
import uvicorn
import shutil
app = FastAPI()
@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
   with open(file.filename, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
   return {"filename": file.filename}

if __name__ == "__main__":
    uvicorn.run("maxcompressor:app")