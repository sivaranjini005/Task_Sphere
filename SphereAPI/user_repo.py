from sqlmodel import Session
from sqlalchemy import select, delete
from fastapi import HTTPException, status
from database import get_session
from models import User, UserBase, UserResponse, UserCreate, UserUpdate

class UserRepo:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, data:UserCreate) -> User:
        user = User(**data.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return UserBase.model_validate(user)

    def get_user(self, user_id:int) -> UserResponse:
        user = self.session.get(User, user_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        
        return UserResponse.model_validate(user)

    def update_user(self, user_id:int, data:UserUpdate) -> UserResponse:
        user = self.session.get(User, user_id)

        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
        data = data.dict(exclude_unset=True)
        
        for key, value in data.items():
            setattr(user, key, value)
        
        self.session.commit()
        self.session.refresh(user)
        return UserResponse.model_validate(user)

    def delete_user(self, user_id:int):
        user = self.session.get(User, user_id)

        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= 'User not found')
        self.session.delete(user)
        self.session.commit()
        return {'Message:User deleted successfully'}



    







