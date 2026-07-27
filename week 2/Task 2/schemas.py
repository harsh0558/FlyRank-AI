from pydantic import BaseModel, ConfigDict
import uuid

class createTaskSchema(BaseModel):
    title: str
    done:bool = False

class createTaskResponse(BaseModel):
    id: uuid.UUID
    title: str
    done: bool

    model_config = ConfigDict(from_attributes=True)