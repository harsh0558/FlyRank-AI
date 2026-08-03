from pydantic import BaseModel, EmailStr

class signupModel(BaseModel):
    email:EmailStr
    password: str


class loginModel(BaseModel):
    email:EmailStr
    password: str