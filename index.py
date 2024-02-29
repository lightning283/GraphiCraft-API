from fastapi import FastAPI, File, UploadFile
import shutil
import shutil
app = FastAPI(title="File Uploader")

@app.get("/")
async def root():
    return {"Hello" : "world"}
@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
   with open(file.filename, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
   return {"filename": file.filename}

# if __name__ == "__main__":
#     uvicorn.run("maxcompressor:app")