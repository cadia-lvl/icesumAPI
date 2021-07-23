
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse
from pydantic import BaseModel
from typing import Optional

import traceback
import sys
sys.path.insert(0, "/usr/src/app/icesum")
from icesum import Summarizer

class SummerizerInput(BaseModel):
    type: Optional[str] = "text"
    content: str
    features: Optional[dict] = {"summary_length": 75}


summarizer = Summarizer('icesum/models/mbl-cnn-s2s.pth')

__version__ = 0.1

app = FastAPI(
    title="icesum",
    description="Sumerizes icelandic articles"
)

@app.get('/', response_class=HTMLResponse)
def home() -> str:
    return """
<html>
    <head><title>icesum API</title></head>
    <body>
        <h1>icesum API Server v{0}</h1>
        <ul><li><a href="/docs">Documentation</a></li></ul>
    </body>
</html>
""".format(__version__)

@app.post('/summarizer')
def summeriser(request: SummerizerInput):
    return summerizer_impl(request.content, request.features["summary_length"])

@app.post('/summarizer/impl')
def summerizer_impl(article : str, summary_length : Optional[int] = 75): 
    try:
        summary = summarizer.predict(article, summary_length=summary_length)
    except RuntimeError:
        if len(article) < 15:
            response = { 
                "code": "elg.summarizer.low.article",
                "text": "The article length must be at least 15 characters long ",
                "params": ["message", "summary"],
                "detail":{'traceback':traceback.format_exc()}
            }
        else: 
            response = { 
                "code": "elg.summarizer.low.summary",
                "text": "The summary length "+str(summary_length)+" is too small for the article length " +str(len(article)),
                "params": ["message", "summary"],
                "detail":{'traceback':traceback.format_exc()}
            }
        print(response)
        return JSONResponse(content=response)
    response = {"response":{
                "type":"texts",
                "content":summary
        }} 
    return JSONResponse(content=response)
