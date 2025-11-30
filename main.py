from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates('templates')

@app.get('/')
def index():
    return {'hello': 'world'}

@app.get('/test', response_class=HTMLResponse)
def template_test(request: Request):
    context = {}
    return templates.TemplateResponse(
        request=request,
        name='test.html',
        context=context
    )

