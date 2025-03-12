from bark_guard_api.bark_recognition.bark_recognition_interface import BarkRecognitionInterface
from enum import Enum


class BarkRecognitionType(Enum):
    pass


class BarkRecognitionFactory:
    _AVAILABLE_RECOGNIZERS = {}

    def create_bark_recognizer(self, recognizer_type: BarkRecognitionType) -> BarkRecognitionInterface:
        try:
            return self._AVAILABLE_RECOGNIZERS[recognizer_type]()
        except KeyError:
            raise KeyError(f"There is no recognizer: {recognizer_type}")
