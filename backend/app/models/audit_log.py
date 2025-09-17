from pydantic import BaseModel

class AuditLog(BaseModel):
    id: int
    tenant_id: int
    action: str
    user_id: int
    timestamp: str
    details: dict
