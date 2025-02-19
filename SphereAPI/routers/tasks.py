from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from typing import List
from models import User, Task, Taskcreate, TaskResponse, UserResponse, TaskUpdate
from task_repo import TaskRepo
from database import get_session

task_router = APIRouter(prefix='/tasks',
                 tags=['tasks'],
                 responses={404:{'description':'not found'}})
def get_task_repo(session:Session = Depends(get_session)) -> TaskRepo:
    return TaskRepo(session=session)


@task_router.post('/', response_model= TaskResponse, status_code=status.HTTP_201_CREATED)
def task_create(data: Taskcreate, user_id:int, repo: TaskRepo = Depends(get_task_repo)):
    new_task = repo.create_task(data = data, user_id= user_id)
    return new_task

@task_router.get('/users/{user_id}', response_model=List[TaskResponse], status_code = status.HTTP_200_OK)
def list_task(user_id:int, repo: TaskRepo = Depends(get_task_repo)):
    tasks = repo.get_task_by_user(user_id)
    return tasks

@task_router.get('/{task_id}', response_model=TaskResponse, status_code=status.HTTP_200_OK)
def task_by_id(task_id:int, repo: TaskRepo = Depends(get_task_repo)):
    task = repo.get_task_by_id(task_id)
    return task

@task_router.patch('/{task_id}', response_model= TaskResponse, status_code=status.HTTP_202_ACCEPTED)
def task_update(task_id:int, data:TaskUpdate, repo: TaskRepo = Depends(get_task_repo)):
    task = repo.update_task(task_id, data)
    return task

@task_router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def task_delete(task_id:int, repo: TaskRepo = Depends(get_task_repo)):
    repo.delete_task(task_id)
    return {'message':'task deletion successfull'}