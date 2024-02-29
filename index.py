from fastapi import FastAPI, File, UploadFile
import shutil
import os
from PIL import Image
from starlette.responses import FileResponse
app = FastAPI(title="File Uploader")

@app.get("/")
async def root():
    return {"Hello" : "world"}

@app.get("/delete")
async def clearStorage():
    shutil.rmtree("uploads/")
    return {"success"}
        
@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
    shutil.rmtree("uploads/")
    os.mkdir("uploads/")
    with open(file.filename, "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
    filename = file.filename
    shutil.move(filename , "uploads/")
    file = "uploads/" + filename
    image = Image.open(file)
    image = image.convert("L")
    image.save(f"uploads/{filename}")
    return {"file converted successfully"}

@app.get("/download/{file_name}")
async def download_file(file_name: str):
    file_path = f"uploads/{file_name}"
    response = FileResponse(file_path, media_type="application/octet-stream", filename=file_name)
    return response , os.remove("uploads/" + file_name)

# if __name__ == "__main__":
#     uvicorn.run("maxcompressor:app")