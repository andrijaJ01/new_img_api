from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import FileResponse
from random import randint
import string
import random
import os

IMAGEDIR = "img/"

app = FastAPI()

IDS=[]

files = os.listdir(IMAGEDIR)
for f in files:
    
    IDS.append(os.path.splitext(f)[0])

@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
    file.filename=f'{id}.jpg'

    contents = await file.read()  # <-- Important!
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)
    IDS.append(id)
    return id

@app.get("/images/{id}")
async def read_img(id):
    path = f"{IMAGEDIR}{id}.jpg"
    return FileResponse(path)

@app.get('/image/list')
async def list_id():
    return IDS
    
"""
I can't feel your hair, the river streaming down
Out of your head and into my open lap.
It once was such silk, always soft to feel,
But now so sparse and wired.
How frayed, such disarray.

I can't feel your face, the mask so perfect
Upon your head and kept so flawless.
It once was porcelain, almost mystical,
But now so torn and broken.
How cracked, so out of place.

I can't feel your hand, a thing so fragile
That it might break if looked at wrong.
It once was dainty, so delicate,
But now so bent and shattered.
How singed, so pulverized.

I can't feel your touch, something I've loved
Ever since we had once met long ago.
It once was stimulation, exhilarating,
But now so gone and so far away.
How far could it possibly be?

I can't feel your pulse, the thing I miss most.

I can't feel.
I can't.

"""

