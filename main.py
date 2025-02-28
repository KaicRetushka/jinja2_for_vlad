from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

from backend.pydantic_classes import BodyAddUser, ReturnDetail
from backend.database import select_all_login, insert_user

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"], 
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

templates = Jinja2Templates(directory='frontend/templates')

app.mount('/static', StaticFiles(directory='frontend/static'), name='static')


@app.get('/')
async def give_glav_str(request: Request):
    list_users = select_all_login()
    return templates.TemplateResponse('index.html', {'request': request, 'list_users': list_users})

@app.get('/reg')
async def give_reg_str(request: Request):
    return templates.TemplateResponse('reg.html', {'request': request})

@app.post('/reg')
async def add_user(body: BodyAddUser) -> ReturnDetail:
    response = insert_user(body.login, body.name, body.surname, body.password)
    if response:
        return {'detail': 'Вы успешно вошли'}
    raise HTTPException(status_code=400, detail='Такой логин уже занят')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)