from fastapi import APIRouter

router = APIRouter(prefix="/analysis", tags=["analysis"])


@router.get("/is-barking")
def is_barking():
    pass


@router.post("/put-values")
async def put_values(user_id, sound):
    pass
