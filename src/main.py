from fastapi import FastAPI
from config import settings
from src.user.router import user_router
from src.products.router import router as product_router

app = FastAPI(
    title='Ecommerce API',
    version='0.0.1'
)

app.include_router(user_router)
app.include_router(product_router)


@app.get('/')
async def root():
    return {'msg': 'Hello World'}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {'msg': f'Hello {name}'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', debug=True, reload=True)
