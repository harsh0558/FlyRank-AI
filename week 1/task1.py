from fastapi import FastAPI, HTTPException

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

@app.get('/')
def home():
    return {
        'message': "hello world"
    }

@app.get("/tasks")
def tasks():
    return {
        "all_tasks": in_memory
    }

@app.get("/tasks/{task_id}")
def task(task_id:int):
    for t in in_memory:
        if t.get('id') == task_id:
            return t
    
    return HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.post("/tasks")
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

    return HTTPException(
        status_code= 201,
        detail='task added succesfully'
    )


@app.get("/health")
def health():
    return {
        "status":"ok"
    }