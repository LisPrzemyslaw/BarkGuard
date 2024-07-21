from abc import ABC, abstractmethod


class SoundRecorderInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def record(self, duration: int) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def get_audio(self) -> bytes:
        pass

    @abstractmethod
    def play_audio(self, audio: bytes) -> None:
        pass

    @abstractmethod
    def delete_audio(self) -> None:
        pass

    @abstractmethod
    def get_audio_duration(self) -> int:
        pass
