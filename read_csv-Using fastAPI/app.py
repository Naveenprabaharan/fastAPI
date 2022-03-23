from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pandas as pd


app = FastAPI()
templates = Jinja2Templates(directory="templates/")

dataset = pd.read_csv('animall.csv')
X = dataset.iloc[: , :].values

i = 0
 

@app.get('/')
def read_form():
    return 'hello world'


@app.get("/form")
def form_post(request: Request):
    image1 = X[i][0]
    image2 = X[i][1]
    print(image1,image2)
    return templates.TemplateResponse('form.html', context={'request': request,'img1':image1, 'img2':image2})


@app.post("/form")
def form_post(request: Request):
    global i
    i = i+1
    image1 = X[i][0]
    image2 = X[i][1]
    print(image1,image2)
    return templates.TemplateResponse('form.html', context={'request': request,'img1':image1, 'img2':image2})