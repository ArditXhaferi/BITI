from replicate.client import Client
from typing import Union
from fastapi import FastAPI
from googletrans import Translator
import uvicorn
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:5500",
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=origins)
]

app = FastAPI(middleware=middleware)

@app.get("/{text}")
async def read_item(text: str):
    translator = Translator()
    translation = translator.translate(text, src='sq', dest='en')
    client = Client(api_token="af4692633d54a789482d40eb9c2651556cc040c7")
    model = client.models.get("stability-ai/stable-diffusion")
    output_url = model.predict(prompt=translation.text)[0]
    return {"url": output_url}

if __name__ == '__main__':
    uvicorn.run(app, port=5000, host='127.0.0.1')