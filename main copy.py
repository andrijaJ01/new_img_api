from fastapi import FastAPI, File, UploadFile
import aiofiles
app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    async with aiofiles.open(f"img/{file.filename}",'wb') as f:
        while content := await file.read(2048):
            await f.write(content)
    return {"RESULT": "OK"}
    