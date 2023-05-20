from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. database import SessionLocal, engine, get_db
from app.database import get_db
from .. import models, schemas, utility
from sqlalchemy.orm import session

router = APIRouter(
    prefix="/users",
    tags=['User']
)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: session = Depends(get_db)):
    # hash user password - user.password
    hashed_password = utility.hash(user.password)
    user.password = hashed_password
    # done hashing password

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} not found")
    return user
