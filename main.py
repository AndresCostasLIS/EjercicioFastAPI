
from fastapi import FastAPI

app = FastAPI(titile= "Ejercicio API")

@app.get("/test")
def test():
    return {"message:" "hello world"}