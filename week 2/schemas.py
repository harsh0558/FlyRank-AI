from pydantic import BaseModel

class ValidateTask(BaseModel):
    id: int
    title: str
    done: bool