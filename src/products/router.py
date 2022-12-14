from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src import db
from . import schemas
from . import services
from . import validator

router = APIRouter(
    tags=['Products'],
    prefix='/products',
)


@router.post('/category', status_code=status.HTTP_201_CREATED, response_model=schemas.ListCategory)
async def create_category(request: schemas.Category, database: Session = Depends(db.get_db)):
    new_category = await services.create_new_category(request, database)
    return new_category


@router.get('/category', status_code=status.HTTP_200_OK, response_model=List[schemas.ListCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    return await services.get_all_categories(database)


@router.get('/category/{category_id}', status_code=status.HTTP_200_OK, response_model=schemas.ListCategory)
async def get_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await services.get_category_by_id(category_id, database)


@router.delete('/category/{category_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category_by_id(category_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_category_by_id(category_id, database)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ProductListing)
async def create_product(request: schemas.Product, database: Session = Depends(db.get_db)):
    category = await validator.verify_category_exist(request.category_id, database)
    if not category:
        raise HTTPException(
            status_code=400,
            detail="You have provided invalid category id.",
        )

    product = await services.create_new_product(request, database)
    return product


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[schemas.ProductListing])
async def get_all_products(database: Session = Depends(db.get_db)):
    return await services.get_all_products(database)
