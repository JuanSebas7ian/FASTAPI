from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Hola FastAPI!"


@app.get("/url")
async def url():
    return {"url": "estoy desplegando un servidor"}
