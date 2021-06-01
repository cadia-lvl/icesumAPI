
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse


import sys
sys.path.insert(0, "/usr/src/app/icesum")
from icesum import Summarizer
summarizer = Summarizer('icesum/models/mbl-cnn-s2s.pth')

__version__ = 0.1

app = FastAPI()

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

@app.get('/summarizer')
def home(article : str, summery_length : Optional[int] = 75): 
    summary = summarizer.predict(article, summary_length=summery_length)
    return Response(content=summary, media_type="txt")
