from fastapi import FastAPI

from app.routes import items, auth, webhooks

app = FastAPI()

app.include_router(auth.router)
app.include_router(items.router)
app.include_router(webhooks.router)

@app.get("/")
def read_root():
    return {"msg": "Pawnshop AI Backend"}