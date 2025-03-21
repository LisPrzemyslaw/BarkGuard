from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from bark_guard_api.web_interface.routers import users, analysis

app = FastAPI()

app.include_router(users.router)
app.include_router(analysis.router)


@app.get("/")
def root() -> JSONResponse:
    """
    This function is a main endpoint of the API. It returns a welcome message.

    :return: json response with status code and message
    """
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Welcome to the BarkGuard! API docs are available at /docs."})
