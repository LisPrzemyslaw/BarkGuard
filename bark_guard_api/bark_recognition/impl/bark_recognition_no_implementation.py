from bark_guard_api.bark_recognition.bark_recognition_interface import BarkRecognitionInterface
import numpy as np


class BarkRecognitionNoImplementation(BarkRecognitionInterface):
    def __init__(self):
        super().__init__()

    def recognize_bark(self, audio: np.ndarray) -> bool:
        """
        This function is a placeholder for the bark recognition implementation. It always returns False.

        :param audio: unused parameter, by default of type np.ndarray, but actually it does not matter
        :return: always False
        """
        return False
