# BarkGuard
BarkGuard is a tool to help you manage your dog's barking. It uses a device with microphone to detect barking and 
send a notification to your phone. It also has a web interface to see the barking history and configure the device.

## Modules
The project is splitted into three main folder.
- `bark_guard_api` is the backend of the project. It is a FastAPI application that serves the web interface and the API. This module is responsible for the communication with the database and the notification service.
- `bark_guard_client` is the client of the project for windows and linux operating systems. It is a Python application that runs innitially on the Dell Wyse and is responsible for recording the audio and sending it to the backend.
- `bark_guard_app` is the android application that receives the notifications from the backend and shows the barking history. The app also can be used as a client to
record the audio and send it to the backend.



## Future Features
- [ ] Add a speaker to play a sound when the dog barks
- [ ] Add a camera to take a picture of the dog when it barks