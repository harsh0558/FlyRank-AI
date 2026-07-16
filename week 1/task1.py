from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

in_memory = [
    {
        "id":1,
        "title":'task1',
        "done": True
    },
    {
        "id":2,
        "title":'task2',
        "done": True
    },
    {
        "id":3,
        "title":'task3',
        "done": False
    }
]
next_id = 4

class taskSchema(BaseModel):
    id:int
    title:str
    done:bool

@app.get('/', summary="Home endpoint")
def home():
    return {
        'message': "hello world"
    }

@app.get("/tasks", summary="Get all tasks")
def tasks():
    return {
        "all_tasks": in_memory
    }

@app.get("/tasks/{task_id}", summary="Get a task by ID")
def task(task_id:int):
    for t in in_memory:
        if t.get('id') == task_id:
            return t
    
    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.post("/tasks", summary="Create a new task")
def add_task(title:str | None):
    global next_id
    if title is None:
        raise HTTPException(
            status_code=400,
            detail='title not provided'
        )

    in_memory.append(
        {
            "id": next_id,
            'title': title,
            'done': False
        }
    )

    next_id +=1

    raise HTTPException(
        status_code= 201,
        detail='task added succesfully'
    )


@app.put("/tasks/{task_id}", summary="Update an existing task")
def update(task:taskSchema):
    update_task = None
    
    for t in in_memory:
        if t.get('id') == task.id:
            update_task = t
            break
    
    if update_task is None:
        raise HTTPException(
            status_code=404,
            detail= 'task not avaliable'
        )
    t['title'] = task.title
    t['done'] = task.done

    return {
        'updated task': t
    }

@app.delete('/tasks/{task_id}', summary="Delete a task")
def delete(task_id:int):
    for t in in_memory:
        if t.get('id') == task_id:
            in_memory.remove(t)
            return {
                'message':'task removed successfully'
            }
    
    raise HTTPException(
        status_code=404,
        detail= "couldn't find task"
    )

@app.get("/health", summary="Check API health")
def health():
    return {
        "status":"ok"
    }