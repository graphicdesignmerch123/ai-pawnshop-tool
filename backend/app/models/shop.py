from pydantic import BaseModel

class Shop(BaseModel):
    id: int
    tenant_id: int
    name: str
    logo_url: str = None
    theme: dict = None
