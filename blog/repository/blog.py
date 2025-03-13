from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(db: Session, request: schemas.Blog):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(db: Session, id: int, request: schemas.Blog):
    # updated = db.query(models.Blog).filter(models.Blog.id == id).update(
    #     {'title': f'{request.title}', 'body': f'{request.body}'}, synchronize_session=False)
    blog = db.query(models.Blog).filter(
        models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog {id} not found')
    blog.update(request.model_dump())
    db.commit()
    return 'updated'


def show(db: Session, id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f'Blog {id} not found'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog {id} not found')
    return blog
