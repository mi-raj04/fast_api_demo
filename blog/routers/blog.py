from fastapi import APIRouter, Depends, status, HTTPException, Response
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db


@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.showBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.showBlog)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(db, id)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(db, id)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, response: Response, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(db, id, request)
