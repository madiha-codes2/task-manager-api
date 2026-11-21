from fastapi import FastAPI, HTTPException
from app.schemas import TaskCreate, TaskUpdate
from typing import Optional
from app.models import create_tables, insert_task, get_all_tasks, get_task_by_id, update_task as update_task_db, delete_task as delete_task_db

app = FastAPI()
create_tables()

@app.get("/")
def home():
    return {"message": "Welcome to Task Manager API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Temporary storage for tasks
tasks = {}
next_task_id = 1

@app.post("/tasks")
def create_task(task: TaskCreate):

    task_id = insert_task(
        task.title,
        task.description,
        task.completed
    )

    return {
        "id": task_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }

@app.get("/tasks")
def get_tasks(completed: Optional[bool] = None):

    all_tasks = get_all_tasks()

    if completed is None:
        return all_tasks

    return [
        task for task in all_tasks
        if bool(task["completed"]) == completed
    ]

@app.get("/tasks/{task_id}")
def get_task(task_id: int):

    task = get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):

    existing_task = get_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    update_task_db(
        task_id,
        updated_task.title,
        updated_task.description,
        updated_task.completed
    )

    return get_task_by_id(task_id)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    rows_deleted = delete_task_db(task_id)

    if rows_deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task deleted successfully"
    }