from fastapi import APIRouter, Depends

from bark_guard_api.web_interface.models.models import AudioRequest
from bark_guard_api.web_interface.dependencies import verify_jwt
from bark_guard_api.database.session import db_session
from bark_guard_api.database.tables.tables import User, Subscription
router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    dependencies=[Depends(verify_jwt)]  # TODO verify if this is better than user_id directly in the function
)


@router.get("/is-barking")
def is_barking():
    raise NotImplementedError


@router.post("/put-values")
async def put_values(sound: AudioRequest, user_id: int = Depends(verify_jwt)):
    raise NotImplementedError
