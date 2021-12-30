from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    text:str
        
app = FastAPI()
classifier = pipeline("summarization")

@app.get("/")
def root():
    return {"Hello": "World"}

@app.put("/translator")
def translator(item: Item):
    return {"translator": classifier(item.text)}
