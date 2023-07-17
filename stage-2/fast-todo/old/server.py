from fastapi import FastAPI, status, HTTPException
import json, sqlite3

app = FastAPI()

class DataClient:
    def __init__(self) -> None:
        connection = sqlite3.connect("./todo.db")
        cursor = connection.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INT PRIMARY KEY,
                title VARCHAR(256),
                completed INT
            );
        """)

    def get_tasks(self) -> list:
        connection = sqlite3.connect("./todo.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        
        cursor.execute(
            "SELECT * FROM tasks;"
        )
        
        return cursor.fetchall()

    def get_task(self, task_id: int) -> dict:
        connection = sqlite3.connect("./todo.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        
        cursor.execute(
            f"SELECT * FROM tasks WHERE id = {task_id};"
        )
        
        return cursor.fetchone()
        
    def update_task(self, task_id: int, task: dict) -> None:
        connection = sqlite3.connect("./todo.db")
        cursor = connection.cursor()
        
        cursor.execute(
            f"UPDATE tasks SET id = {task['id']}, name = {task['name']}, completed = {task['completed']} WHERE id = {task_id};"
        )

    def write_tasks(self, tasks: list) -> int:
        return open("./tasks.json", "w").write(
            json.dumps(tasks)
        )

data_client = DataClient()

@app.get("/")
def read_root() -> dict:
    return {
        "info": "This is simple todo app for managing your daily tasks",
        "tasks_list": "/tasks"
    }

@app.get("/tasks/")
def read_tasks() -> list:
    return data_client.get_tasks()

@app.get("/tasks/{task_id}")
def read_task(task_id: int, q = None) -> dict:
    if data_client.get_task(task_id):
        return data_client.get_task(task_id)
    else:
        raise HTTPException(status_code=404, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")

@app.post("/tasks/")
def create_task(task: dict) -> str:
    tasks: list = data_client.get_tasks()
    tasks.append(task)
    data_client.write_tasks(tasks)

    return "Received"

@app.put("/tasks/{task_id}")
def update_task(task_id: int, new_task: dict) -> dict:
    data_client.update_task(task_id, new_task)
    
    return "Updated"

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int) -> int:
    tasks: list = data_client.get_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return task_id

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{status.HTTP_404_NOT_FOUND} - Task not found")
