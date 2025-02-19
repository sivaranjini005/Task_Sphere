from sqlmodel import Session
from sqlalchemy import select, delete
from fastapi import HTTPException, status
from database import get_session
from typing import List
from models import Task, User, TaskResponse, Taskcreate, TaskUpdate

class TaskRepo:
    def __init__(self, session: Session):
        self.session = session

    def create_task(self, data:Taskcreate, user_id:int) -> Taskcreate:
        values = data.model_dump()
        values['user_id'] = user_id
        new_task = Task(**values)

        self.session.add(new_task)
        self.session.commit()
        self.session.refresh(new_task)

        return TaskResponse.model_validate(new_task)

    def get_task_by_user(self, user_id:int) -> List[TaskResponse]:
        statement = select(Task).where(Task.user_id == user_id)
        result = self.session.execute(statement)
        tasks = result.scalars().all()
        return [TaskResponse.model_validate(task) for task in tasks]

    def get_task_by_id(self, task_id:int):
        task = self.session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'task not found')
        return TaskResponse.model_validate(task)

    def update_task(self, task_id:int, data:TaskUpdate):
        task = self.session.get(Task, task_id)

        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'task not found')
        data = data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(task, key, value)
        self.session.commit()
        self.session.refresh(task)
        return TaskResponse.model_validate(task)
    
    def delete_task(self, task_id:int):
        task = self.session.get(Task, task_id)

        if not task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='task not found')
        self.session.delete(task)
        self.session.commit()
        

    



