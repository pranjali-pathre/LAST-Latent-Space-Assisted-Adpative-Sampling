from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from typing import List
import shutil
import subprocess
import os
import pickle
import io
import numpy as np

from starlette.responses import FileResponse
app = FastAPI()

@app.post("/files/")
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

@app.post("/uploadpdb/")
async def upload_pdb(file: UploadFile = File(...)):
    if(not os.path.exists("./inputs")):
        os.mkdir("./inputs")
    extension = file.filename.rsplit('.', 1)[-1]
    if(extension not in ['pdb']):
        return {"Message": "Protein files of format ['pdb'] are allowed."}
    with open("./inputs/1ake."+extension, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"Message": "Protein file uploaded successfully."}

@app.post("/uploadtop/")
async def upload_top(file: UploadFile = File(...)):
    if(not os.path.exists("./inputs")):
        os.mkdir("./inputs")
    extension = file.filename.rsplit('.', 1)[-1]
    if(extension not in ['prmtop']):
        return {"Message": "Files of format ['prmtop'] are allowed."}
    with open("./inputs/1ake."+extension, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"Message": "Protein file uploaded successfully."}

@app.post("/uploadinp/")
async def upload_inp(file: UploadFile = File(...)):
    if(not os.path.exists("./inputs")):
        os.mkdir("./inputs")
    extension = file.filename.rsplit('.', 1)[-1]
    if(extension not in ['inpcrd']):
        return {"Message": "Protein files of format ['inpcrd'] are allowed."}
    with open("./inputs/1ake."+extension, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"Message": "Protein file uploaded successfully."}

@app.post("/run/")
async def run():
    os.system('chmod +x ./run.sh')
    os.system('./run.sh 1ake 4 5')

    res = []
    prefixed = [filename for filename in os.listdir('./results/results/') if filename.startswith("1ake_r")]
    prefixed = prefixed.sort()
    print(prefixed)

    for nn in range(0, 4):
        file_name ='./results/results/1ake_r' + str(nn) + '_latents.pkl'
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
        data = np.array(data)
        print(data.shape)
        res.append(data.tolist())

    return {"response": res}
