from blog.routers import authentication
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


# ? Code below was moved to respective routers. Left here for reference later but hidden by block comment.
"""
    # //def get_db():
    # //    db = SessionLocal()
    # //    try:
    # //        yield db
    # //    finally:
    # //        db.close()


    # //@app.post('/blog', status_code=status.HTTP_201_CREATED, tags=['blogs','post'])
    # //def create(request : schemas.Blog, db : Session = Depends(get_db)):
    # //    new_blog = models.Blog(title=request.title, body=request.body, user_id = 1) #!temp hardcoding
    # //    db.add(new_blog)
    # //    db.commit()
    # //    db.refresh(new_blog)
    # //    return new_blog

    # //@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=['blogs','delete'])
    # //def destroy(id, db : Session = Depends(get_db)):
    # //    blog = db.query(models.Blog).filter(models.Blog.id == id)

    # //    if not blog.first():
    # //        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
        
    # //    blog.delete()
    # //    db.commit()
    # //    return Response(status_code=status.HTTP_204_NO_CONTENT)


    # //@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=['blogs','put'])
    # //def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
    # //    blog = db.query(models.Blog).filter(models.Blog.id == id)

    # //    if not blog.first():
    # //        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    # //    blog.update(request.dict())

    # //    db.commit()
    # //    return 'updated succesfully'

    # //# //@app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs','get'])
    # //# //def all_blogs(db : Session = Depends(get_db)):
    # //# //    blogs = db.query(models.Blog).all()
    # //# //    return blogs



    # //@app.get('/blog/{id}',status_code=status.HTTP_200_OK,response_model=schemas.ShowBlog, tags=['blogs','get'])
    # //def show(id, response : Response, db : Session = Depends(get_db)):
    # //    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    # //    if not blog:
    # //        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Blog with the id {id} is not available")
    # //        # // response.status_code = status.HTTP_404_NOT_FOUND
    # //        # // return {'detail': f"Blog with the id {id} is not available"}

    # //    return blog




    # //@app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['user','post'])
    # //def create_user(request: schemas.User, db : Session = Depends(get_db)):
    # //    new_user = models.User(name = request.name, email = request.email, password = Hash.bcrypt(request.password))
    # //    db.add(new_user)
    # //    db.commit()
    # //    db.refresh(new_user)
    # //    return new_user


    # //@app.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser, tags=['user','get'])
    # //def get_user(id:int, db: Session = Depends(get_db)):
    # //    user = db.query(models.User).filter(models.User.id == id).first()

    # //    if not user:
    # //         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"User with the id {id} is not available")
    # //    return user
"""