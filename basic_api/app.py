from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get('/')
def read_form():
    return 'hello world'


@app.get("/form")
def form_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})


@app.post("/form")
def form_post(request: Request, name: str = Form(...),content: str = Form(...)):
    name1 = name
    content1 = content
    return templates.TemplateResponse('send.html', context={'request': request, 'name': name1, 'content':content1})