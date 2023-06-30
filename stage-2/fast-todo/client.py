import requests

CRUD: list = ["create", "read", "update", "delete"]
PROMPTS: dict = {
    "main": """
+-- Choose CRUD operation
|
+----- 1. Create
+----- 2. Read
+----- 3. Update
+----- 4. Delete
|
+-[1-4]-> """,

    "create": """
+-- Create
+----- Create new task
|
+----- Example: 1, "Task 1", 0
|
+-[id, task, completed]-> """,

    "update": """
+-- Update
+----- Update task with matching ID
|
+----- Example: 1, "Task 1", 0
|
+-[id, task, completed]-> """,

    "delete": """
+-- Delete
+---- Delete task with matching ID
|
+-[id]-> """
}
VALID_INPUTS: dict = {
    "main": ["1", "2", "3", "4"]
}

class TaskClient:
    BASE_URL = "http://127.0.0.1:8000/tasks/"

    def create_task(self, **task) -> dict:
        return requests.post(f"{TaskClient.BASE_URL}", json=task).json()

    def read_task(self, task_id) -> dict:
        return requests.get(f"{TaskClient.BASE_URL}{task_id}").json()

    def read_tasks(self) -> list:
        return requests.get(f"{TaskClient.BASE_URL}").json()

    def update_task(self, task_id, **task) -> dict:
        return requests.put(f"{TaskClient.BASE_URL}{task_id}", json=task).json()

    def delete_task(self, task_id) -> int:
        return requests.delete(f"{TaskClient.BASE_URL}{task_id}").json()
    
def prompt_crud(client: TaskClient, operation: str = "create") -> None:
    if operation == "create":
        raw_inputs: str = input(PROMPTS["create"]).split(",")
        
        try:
            task_id: int = int(raw_inputs[0].strip(" "))
            task_title: str = raw_inputs[1].strip(" ").strip("\"").strip("'")
            completed: bool = bool(int(raw_inputs[2].strip(" ")))
        except (ValueError, IndexError):
            prompt_crud(client, operation)
            return None
        
        client.create_task(id = task_id, title = task_title, completed = completed)
    
    if operation == "read":
        if len(client.read_tasks()) < 1:
            print("Nothing to read")
            
        for task in client.read_tasks():
            print(task)
    
    if operation == "update":
        raw_inputs: str = input(PROMPTS["update"]).split(",")
        
        try:
            task_id: int = int(raw_inputs[0].strip(" "))
            task_title: str = raw_inputs[1].strip(" ").strip("\"").strip("'")
            completed: bool = bool(int(raw_inputs[2].strip(" ")))
        except (ValueError, IndexError):
            prompt_crud(client, operation)
            return None

        client.update_task(task_id, id = task_id, title = task_title, completed = completed)
    
    if operation == "delete":
        raw_inputs: str = input(PROMPTS["delete"])
        
        try:
            task_id: int = int(raw_inputs.strip(" "))
        except ValueError:
            prompt_crud(client, operation)
            return None
        
        client.delete_task(task_id)

def main() -> None:
    RUN: bool = True
    client = TaskClient()

    while RUN:
        choice: str = input(PROMPTS["main"])
        
        if choice in VALID_INPUTS["main"]:
            try:
                prompt_crud(
                    client,
                    CRUD[int(choice)-1]
                )
            except (EOFError, KeyboardInterrupt):
                print("\n")
                continue
            
    
if __name__ == "__main__":
    try: 
        main()
    except (EOFError, KeyboardInterrupt):
        print("\n\nExiting...\n")