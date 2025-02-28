from pydantic import BaseModel

class BodyAddUser(BaseModel):
    login: str
    name: str
    surname: str
    password: str

class ReturnDetail(BaseModel):
    detail: str