from fastapi import FastAPI
from bark_guard_api.web_interface.routers import users, analysis

app = FastAPI()

app.include_router(users.router)
app.include_router(analysis.router)


@app.get("/")
def root():
    return {"message": "Welcome to the BarkGuard!"}
