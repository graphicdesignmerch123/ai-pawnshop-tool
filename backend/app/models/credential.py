from pydantic import BaseModel

class Credential(BaseModel):
    id: int
    tenant_id: int
    provider: str
    credentials: dict
