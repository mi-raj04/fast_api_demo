# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel

# app = FastAPI()


# @app.get('/')
# def index():
#     return {'data': {'name': 'raj saija'}}


# @app.get('/about')
# def about():
#     return {'data': {'about': 'this is about page', 'pages': {'home', 'about', 'contact'}}}


# @app.get('/blog/{id}')
# def blogId(id: int):
#     return {'data': id}


# @app.get('/blog/{id}/comments')
# def comments(id):
#     return {'data': {'comment': {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}}}

# # @app.get('/data')
# # def query(limit: int, sorting: bool):
# #     if sorting:
# #         return {'data': f'limit is {limit} fetched in desending orders'}
# #     else:
# #         return {'data': f'limit is {limit} fetched in assending orders'}


# # @app.get('/data')
# # def query(limit=10, sorting=True):
# #     if sorting:
# #         return {'data': f'limit is {limit} fetched in desending orders'}
# #     else:
# #         return {'data': f'limit is {limit} fetched in assending orders'}


# @app.get('/data')
# def query(limit: int, sorting: Optional[bool] = None):
#     if sorting:
#         return {'data': f'limit is {limit} fetched in desending orders'}
#     else:
#         return {'data': f'limit is {limit} fetched in assending orders'}


# class Blog(BaseModel):
#     titile: str
#     body: str
#     published: Optional[bool]


# @app.post('/blog')
# def create_blog(blog: Blog):
#     return {'data': f'your created blog title is {blog.titile}'}


from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication


from fastapi import FastAPI
from blog import models
from blog.database import engine
from blog.routers import blog, user, authentication


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
