from fastapi import FastAPI, Depends
from routers import tasks
from routers import users

app = FastAPI()

app.include_router(tasks.task_router)
app.include_router(users.user_router)


