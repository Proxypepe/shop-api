from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from src import db
from . import schemas
from . import services
from . import validator

user_router = APIRouter(
    tags=['Users'],
    prefix='/users'
)


@user_router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.DisplayUser)
async def create_user_registration(request: schemas.User, database: Session = Depends(db.get_db)):
    user = await validator.verify_email_exists(request.email, database)
    if user is not None:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    new_user = await services.new_user_register(request, database)
    return new_user


@user_router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.DisplayUser])
async def get_all_users(
        database: Session = Depends(db.get_db),
):
    return await services.all_users(database)


@user_router.get('/{user_id}', status_code=status.HTTP_200_OK, response_model=schemas.DisplayUser)
async def get_user_by_id(
        user_id: int,
        database: Session = Depends(db.get_db),
):
    return await services.get_user_by_id(user_id, database)


@user_router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user_by_id(
        user_id: int,
        database: Session = Depends(db.get_db),
):
    return await services.delete_user_by_id(user_id, database)