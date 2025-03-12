from fastapi import APIRouter, Depends

from bark_guard_api.web_interface.dependencies import verify_jwt

router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    dependencies=[Depends(verify_jwt)]  # TODO verify if this is better than user_id directly in the function
)

...
