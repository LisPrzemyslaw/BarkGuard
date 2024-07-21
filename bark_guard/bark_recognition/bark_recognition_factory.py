from bark_guard.bark_recognition.bark_recognition_interface import BarkRecognitionInterface


class BarkRecognitionFactory:
    _AVAILABLE_RECOGNIZERS = {}

    def create_bark_recognizer(self, recognizer_type: BarkRecognitionInterface) -> BarkRecognitionInterface:
        try:
            return self._AVAILABLE_RECOGNIZERS[recognizer_type]()
        except KeyError:
            raise KeyError(f"There is no recognizer: {recognizer_type}")
