from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def saludar():
    return {"saludar": "hola mundo"}

#comentario
def perro():
    return 5



