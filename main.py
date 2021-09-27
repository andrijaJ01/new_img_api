from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.param_functions import Form
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, UploadFile, Response
from fastapi.responses import FileResponse
from random import randint
import string
import random
import os

app = FastAPI()

IMAGEDIR = "img/"


@app.get("/")
async def main():
    content = """
<body>
<style>
input {
  border: 1px solid #242424;
  border-radius:999px;
  background-color: #f1f1f1;
  padding: 10px;
  font-size: 16px;
}
textarea:focus, input:focus{ border: none; }
</style>
<form action="/images/" enctype="multipart/form-data" method="post">
<input name="file" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


IDS=[]

files = os.listdir(IMAGEDIR)
for f in files:
    
    IDS.append(os.path.splitext(f)[0])

@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(9))
    file.filename=f'{id}.png'

    contents = await file.read() 
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    IDS.append(id)
    content =f"<head><title>SUCCESS</title></head><body>\n<p>To access image go to the<a href='/images/{id}'> this link</a></p></body>"
    return HTMLResponse(content=content)

@app.get("/images/{id}")
async def read_img(id):
    path = f"{IMAGEDIR}{id}.png"
    return FileResponse(path)

@app.get('/image/list')
async def list_id():
    return IDS
