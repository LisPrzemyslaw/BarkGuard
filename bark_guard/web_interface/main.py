from fastapi import FastAPI
from fastapi.responses import Response
import uvicorn
import os
import uvicorn
import cv2

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/image")
def capture():
    # Capture a photo using OpenCV
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    camera.release()

    # Save the captured photo to a file
    photo_path = os.path.join("photos", "photo.jpg")
    cv2.imwrite(photo_path, frame)

    # Process the captured photo if needed
    # ...

    # Return relevant information about the captured photo
    return Response(content=photo_path, media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
