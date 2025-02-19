from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from models import User,UserCreate, UserBase, UserResponse, UserUpdate
from user_repo import UserRepo
from database import get_session

user_router = APIRouter(
    prefix='/users', tags=['users'], 
    responses={404:{'description':'not found'}}
)

def get_user_repo(session:Session = Depends(get_session)):
    return UserRepo(session)

@user_router.post('/', response_model=UserBase, status_code=status.HTTP_201_CREATED)
def user_creation(data:UserCreate, repo:UserRepo = Depends(get_user_repo)):
    new_user = repo.create_user(data)
    return new_user

@user_router.get('/{user_id}', response_model=UserResponse, status_code=status.HTTP_200_OK)
def user_get(user_id: int, repo: UserRepo = Depends(get_user_repo)):
    user = repo.get_user(user_id)
    return user

@user_router.patch('/{user_id}', response_model= UserBase, status_code=status.HTTP_202_ACCEPTED)
def user_update(user_id:int, data:UserUpdate, repo: UserRepo = Depends(get_user_repo)):
    new_user = repo.update_user(user_id, data)
    return new_user

@user_router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def user_deletion(user_id:int, repo: UserRepo = Depends(get_user_repo)):
    delete = repo.delete_user(user_id)
    return delete