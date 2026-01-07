from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Inicia el servidor: uvicorn users:app --reload
# Entidad users
class User(BaseModel):
    id: int
    name: str
    middle_name: str
    last_name: str
    age: int
    url: str


users_list = [
    User(
        id=1,
        name="Jose",
        middle_name="Antonio",
        last_name="Palacio",
        age=30,
        url="https://www.google.com/search?q=Jose+Antonio+Palacio",
    ),
    User(
        id=2,
        name="Maria",
        middle_name="Maria",
        last_name="Paniagua",
        age=31,
        url="https://www.google.com/search?q=Maria+Maria+Paniagua",
    ),
    User(
        id=3,
        name="Pedro",
        middle_name="Pedro",
        last_name="Paniagua",
        age=32,
        url="https://www.google.com/search?q=Pedro+Pedro+Paniagua",
    ),
    User(
        id=4,
        name="Ana",
        middle_name="Isabel",
        last_name="García",
        age=33,
        url="https://www.google.com/search?q=Ana+Isabel+Garcia",
    ),
]


@app.get("/usersjson")
async def usersjson():
    return [
        {
            "name": "Jose",
            "middle_name": "Antonio",
            "last_name": "Palacio",
            "age": 30,
            "url": "https://www.google.com/search?q=Jose+Antonio+Palacio",
        },
        {
            "name": "Maria",
            "middle_name": "Maria",
            "last_name": "Paniagua",
            "age": 31,
            "url": "https://www.google.com/search?q=Maria+Maria+Paniagua",
        },
        {
            "name": "Pedro",
            "middle_name": "Pedro",
            "last_name": "Paniagua",
            "age": 32,
            "url": "https://www.google.com/search?q=Pedro+Pedro+Paniagua",
        },
        {
            "name": "Ana",
            "middle_name": "Isabel",
            "last_name": "García",
            "age": 33,
            "url": "https://www.google.com/search?q=Ana+Isabel+Garcia",
        },
    ]


@app.get("/users")
async def users():
    return users_list


# Path
@app.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se encontro el usuario"}


# Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se encontro el usuario"}
