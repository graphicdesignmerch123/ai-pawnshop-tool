from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Models

class Shop(BaseModel):
    id: int
    tenant_id: int
    name: str
    description: Optional[str] = None

class Listing(BaseModel):
    id: int
    tenant_id: int
    shop_id: int
    title: str
    description: Optional[str] = None
    image_urls: Optional[List[str]] = None
    price: Optional[float] = None
    status: Optional[str] = None

class Credential(BaseModel):
    id: int
    tenant_id: int
    provider: str
    value: str
    metadata: Optional[dict] = None

class AuditLog(BaseModel):
    id: int
    tenant_id: int
    action: str
    user_id: int
    timestamp: str
    details: Optional[dict] = None

app = FastAPI()

# In-memory "databases"
shops = {}
listings = {}
credentials = {}
auditlogs = {}

# SHOP endpoints

@app.post("/shops/", response_model=Shop)
def create_shop(shop: Shop):
    if shop.id in shops:
        raise HTTPException(status_code=400, detail="Shop ID already exists")
    shops[shop.id] = shop
    return shop

@app.get("/shops/{shop_id}", response_model=Shop)
def get_shop(shop_id: int):
    shop = shops.get(shop_id)
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return shop

@app.get("/shops/", response_model=List[Shop])
def list_shops():
    return list(shops.values())

@app.put("/shops/{shop_id}", response_model=Shop)
def update_shop(shop_id: int, shop: Shop):
    if shop_id not in shops:
        raise HTTPException(status_code=404, detail="Shop not found")
    shops[shop_id] = shop
    return shop

@app.delete("/shops/{shop_id}")
def delete_shop(shop_id: int):
    if shop_id not in shops:
        raise HTTPException(status_code=404, detail="Shop not found")
    del shops[shop_id]
    return {"ok": True}

# LISTING endpoints

@app.post("/listings/", response_model=Listing)
def create_listing(listing: Listing):
    if listing.id in listings:
        raise HTTPException(status_code=400, detail="Listing ID already exists")
    listings[listing.id] = listing
    return listing

@app.get("/listings/{listing_id}", response_model=Listing)
def get_listing(listing_id: int):
    listing = listings.get(listing_id)
    if not listing:
        raise HTTPException(status_code=404, detail="Listing not found")
    return listing

@app.get("/listings/", response_model=List[Listing])
def list_listings():
    return list(listings.values())

@app.put("/listings/{listing_id}", response_model=Listing)
def update_listing(listing_id: int, listing: Listing):
    if listing_id not in listings:
        raise HTTPException(status_code=404, detail="Listing not found")
    listings[listing_id] = listing
    return listing

@app.delete("/listings/{listing_id}")
def delete_listing(listing_id: int):
    if listing_id not in listings:
        raise HTTPException(status_code=404, detail="Listing not found")
    del listings[listing_id]
    return {"ok": True}

# CREDENTIAL endpoints

@app.post("/credentials/", response_model=Credential)
def create_credential(credential: Credential):
    if credential.id in credentials:
        raise HTTPException(status_code=400, detail="Credential ID already exists")
    credentials[credential.id] = credential
    return credential

@app.get("/credentials/{credential_id}", response_model=Credential)
def get_credential(credential_id: int):
    credential = credentials.get(credential_id)
    if not credential:
        raise HTTPException(status_code=404, detail="Credential not found")
    return credential

@app.get("/credentials/", response_model=List[Credential])
def list_credentials():
    return list(credentials.values())

@app.put("/credentials/{credential_id}", response_model=Credential)
def update_credential(credential_id: int, credential: Credential):
    if credential_id not in credentials:
        raise HTTPException(status_code=404, detail="Credential not found")
    credentials[credential_id] = credential
    return credential

@app.delete("/credentials/{credential_id}")
def delete_credential(credential_id: int):
    if credential_id not in credentials:
        raise HTTPException(status_code=404, detail="Credential not found")
    del credentials[credential_id]
    return {"ok": True}

# AUDITLOG endpoints

@app.post("/auditlogs/", response_model=AuditLog)
def create_audit_log(audit_log: AuditLog):
    if audit_log.id in auditlogs:
        raise HTTPException(status_code=400, detail="AuditLog ID already exists")
    auditlogs[audit_log.id] = audit_log
    return audit_log

@app.get("/auditlogs/{audit_log_id}", response_model=AuditLog)
def get_audit_log(audit_log_id: int):
    audit_log = auditlogs.get(audit_log_id)
    if not audit_log:
        raise HTTPException(status_code=404, detail="AuditLog not found")
    return audit_log

@app.get("/auditlogs/", response_model=List[AuditLog])
def list_audit_logs():
    return list(auditlogs.values())

@app.put("/auditlogs/{audit_log_id}", response_model=AuditLog)
def update_audit_log(audit_log_id: int, audit_log: AuditLog):
    if audit_log_id not in auditlogs:
        raise HTTPException(status_code=404, detail="AuditLog not found")
    auditlogs[audit_log_id] = audit_log
    return audit_log

@app.delete("/auditlogs/{audit_log_id}")
def delete_audit_log(audit_log_id: int):
    if audit_log_id not in auditlogs:
        raise HTTPException(status_code=404, detail="AuditLog not found")
    del auditlogs[audit_log_id]
    return {"ok": True}