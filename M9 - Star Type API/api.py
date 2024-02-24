from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index_route():
    return {"Health" : "Ok"}