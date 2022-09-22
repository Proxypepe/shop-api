import pytest
from httpx import AsyncClient

from src.auth.jwt import create_access_token
from test.conf_test_db import app
from test.shared.info import category_info, product_info


@pytest.mark.asyncio
async def test_order_listing():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        user_access_token = create_access_token({"sub": "alex@gmail.com"})
        response = await ac.get("/orders/", headers={'Authorization': f'Bearer {user_access_token}'})

    assert response.status_code == 200
