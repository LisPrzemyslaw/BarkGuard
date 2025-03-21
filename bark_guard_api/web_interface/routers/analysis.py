import asyncio
import datetime
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from bark_guard_api.web_interface.models.models import AudioRequest
from bark_guard_api.web_interface.dependencies import verify_jwt
from bark_guard_api.database.session import db_session
from bark_guard_api.database.tables.tables import Subscription
from bark_guard_api.web_interface.bark_guard_session import streaming_sessions, Stream
from bark_guard_api.bark_recognition.bark_recognition_factory import BarkRecognitionFactory

router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],
    dependencies=[Depends(verify_jwt)]  # TODO verify if this is better than user_id directly in the function
)


@router.post("/start-session")
async def start_session(user_id: int = Depends(verify_jwt)) -> JSONResponse:
    """
    This function is used to start session for user. The bark recognizer is created based on the subscription plan.
    Bark recognition is started in the loop. It will be stop when the session is ended or the queue is empty.

    :param user_id: id of the user in db

    :return: json response with status code and message
    """
    streaming_sessions[user_id] = Stream()
    stream: Stream = streaming_sessions[user_id]
    subscription_type = db_session.query(Subscription).filter(Subscription.user_id == user_id).first().plan
    bark_recognizer = BarkRecognitionFactory.create_bark_recognizer(subscription_type)

    while datetime.datetime.now() < stream.start_time + timedelta(seconds=30):  # Wait for the first sound
        if len(stream.records) != 0:
            break
        await asyncio.sleep(1)
    else:
        await end_session()
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT, detail="No sound was uploaded. Session ended.")

    while True:
        if stream.is_session_end:
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Session ended."})
        try:
            sound = stream.records.popleft()
        except IndexError:
            return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Queue is empty."})
        is_barking = bark_recognizer.recognize_bark(sound)
        if is_barking:
            await bark_action()


@router.post("/end-session")
async def end_session(user_id: int = Depends(verify_jwt)) -> JSONResponse:
    """
    This function is used to end session for user. It will stop the stream and delete the session.

    :param user_id: id of the user in db

    :return: json response with status code and message
    """
    stream: Stream = streaming_sessions[user_id]
    stream.is_session_end = True
    await asyncio.sleep(5)
    del streaming_sessions[user_id]
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Session ended."})


@router.post("/put-values")  # TODO change to streaming
async def put_values(sound: AudioRequest, user_id: int = Depends(verify_jwt)) -> JSONResponse:
    """
    This function is used to put values from the stream to the queue.

    :param sound: sound from the stream
    :param user_id: id of the user in db

    :return: json response with status code and message
    """
    try:
        stream: Stream = streaming_sessions[user_id]
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Session not found. First call /start-session")

    stream.records.append(sound.audio)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Sound added to the queue."})


@router.get("/bark-action")
async def bark_action(user_id: int = Depends(verify_jwt)):
    """
    This function is used to get bark action for user. It will send the notification to the user.

    :param user_id: id of user
    """
    pass
