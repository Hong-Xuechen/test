from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

class Item(BaseModel):
    text:str
        
app = FastAPI()
nlp = pipeline("question-answering")

context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script.
"""

result = nlp(question=item.text, context=context)

@app.get("/")
def root():
    return {"Hello": "World"}

@app.put("/question-answering")
def question-answering(item: Item):
    return {"question-answering": result}
