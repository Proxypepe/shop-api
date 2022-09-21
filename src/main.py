from fastapi import FastAPI
from config import settings
from src.user.router import user_router
from src.products.router import router as product_router
from src.orders.router import router as orders_router
from src.cart.router import router as cart_router
from src.auth.router import router as auth_router

app = FastAPI(
    title='Ecommerce API',
    version='0.0.1'
)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(orders_router)
app.include_router(cart_router)
app.include_router(auth_router)


@app.get('/')
async def root():
    return {'msg': 'Hello World'}


@app.get('/hello/{name}')
async def say_hello(name: str):
    return {'msg': f'Hello {name}'}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', debug=True, reload=True)
