from fastapi import FastAPI
from config import settings

app = FastAPI()


@app.get('/')
async def root():
    return {'msg': 'Hello World'}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {'msg': f'Hello {name}'}


if __name__ == '__main__':
    import uvicorn

    print(settings.dict())
    uvicorn.run('main:app', debug=True, reload=True)
