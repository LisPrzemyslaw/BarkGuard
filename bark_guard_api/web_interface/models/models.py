from pydantic import BaseModel


class AudioRequest(BaseModel):
    audio: bytes
    sample_rate: int


class UserRequest(BaseModel):
    email: str
    password: str
