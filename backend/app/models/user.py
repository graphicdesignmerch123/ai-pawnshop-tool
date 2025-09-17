from pydantic import BaseModel

class User(BaseModel):
    id: int
    tenant_id: int
    username: str
    hashed_password: str
