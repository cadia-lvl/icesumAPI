
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse, HTMLResponse
from pydantic import BaseModel
from typing import Optional

import traceback
import sys
sys.path.insert(0, "/usr/src/app/icesum")
from icesum import Summarizer



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

class SummarizerParams(BaseModel):
	summary_length: int = 75

class SummarizerInput(BaseModel):
	type: Optional[str] = "text"
	content: str
	params: SummarizerParams = SummarizerParams()


@app.post('/summarizer')
def summariser(request: SummarizerInput):
	article = request.content
	summary_length = request.params.summary_length
	try:
		summary = summarizer.predict(article, summary_length=summary_length)
	except RuntimeError:
		if len(article) < 15:
			err={"code": "icesum.summarizer.low.article",
				"text": "The article length must be at least 15 characters long ",
				"detail":{'traceback':traceback.format_exc()}
			}
		else: 
			err = { 
				"code": "icesum.summarizer.failed",
				"text": "The summarizer returned an error" ,
				"detail":{'traceback':traceback.format_exc()}
			}
		response = {
			"failure":{
				"errors":[err]
				}
			}
		return JSONResponse(content=response)
	response = {"response":{
				"type":"texts",
				"texts":[{"content":summary}] 
		}} 
	return JSONResponse(content=response)
