from pydantic import BaseModel

class TaskSchema(BaseModel):
    id: int
    title: str
    done: bool

class UpdateTaskSchema(BaseModel):
    title: str
    done: bool