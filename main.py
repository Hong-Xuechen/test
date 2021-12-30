from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    text:str
        
app = FastAPI()
classifier = pipeline("fill-mask","sentence-transformers/all-mpnet-base-v2")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.put("/translator")
def translator(item: Item):
    return {"translator": classifier(item.text)}
