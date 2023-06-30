from typing import Union
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

tasks: list = []

@app.get("/")
def read_root() -> dict:
    return {
        "info": "This is simple todo app for managing your daily tasks",
        "tasks_list": "/tasks"
    }

@app.get("/tasks/")
def read_tasks() -> list:
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int, q = None) -> dict:
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")

@app.post("/tasks/")
def create_task(task: dict) -> str:
    tasks.append(task)
    return "Received"

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_task: dict) -> dict:
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = new_task
            return new_task
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> int:
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return task_id
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")