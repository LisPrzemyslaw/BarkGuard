from abc import ABC, abstractmethod


class BarkRecognitionInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def recognize_bark(self, audio: bytes) -> bool:
        """
        This function should recognize if the audio contains a dog bark.

        :param audio: audio to be recognized

        :return: True if the audio contains a dog bark, False otherwise
        """
        pass
