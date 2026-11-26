from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
app=FastAPI()
client=OpenAI()
model_name="gpt-6.2-astra"
prompt="次のメモを一文で要約して。メモに書かれていないことは足さないで："
class Memo(BaseModel):
    text:str
@app.get("/hello")
def read_root():
    return{"message":"今日はいい天気"}

@app.post("/memos")
def create_memo(memo:Memo):
    response=client.responses.create(model=model_name,input=prompt+memo.text)
    return{"memo":memo.text,"summary":response.output_text}