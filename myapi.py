from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# address domain/path - endpoint
# GET
# POST
# UPDATE
# DELETE

class Todo(BaseModel):
    status: str
    title: str

class UpdateTodo(BaseModel):
    status: Optional[str] = None
    title: Optional[str] = None

todos = {
    1: Todo(status = "Complete", title = "Basketball with friends"),
    2: Todo(status = "Incomplete", title = "Cook dinner")
}


#GET METHOD
@app.get("/get-todo/{id}")
def get_todo(id: int = Path(description="The ID of todo that you want to see")):
    return todos[id]

@app.get("/get-todo-by-title/{title}")
def get_todo_by_title(title: str):
    for todo_id in todos:
        if todos[todo_id].title == title:
            return todos[todo_id]
    return {"error" : "Todo doesn't exist, please put the correct input"}

#POST METHOD
@app.post("/create-todo/{todo_id}")
def add_todo(todo_id: int, todo: Todo):
    if todo_id in todos:
        return {"error: todo already exist!"}
    todos[todo_id] = todo
    return todos[todo_id]

#PUT METHOD
@app.put("/update-todo/{todo_id}")
def update_todo(todo_id: int, todo: UpdateTodo):
    if todo_id not in todos:
        return {"error": "todo is NOT exist!"}
    
    if todo.status != None:
        todos[todo_id].status = todo.status

    if todo.title != None:
        todos[todo_id].title = todo.title

    return todos[todo_id]

#DELETE METHOD
@app.delete("/delete-todo/{todo_id}")
def delete_todo(todo_id: int):
    if todo_id not in todos:
        return {"error: The data is not EXIST!"}
    del todos[todo_id]
    return {"data":"deleted sucessfully!"}