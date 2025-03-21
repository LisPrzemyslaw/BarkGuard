from bark_guard_api.bark_recognition.bark_recognition_interface import BarkRecognitionInterface
from bark_guard_api.bark_recognition.impl.bark_recognition_no_implementation import BarkRecognitionNoImplementation


class BarkRecognitionFactory:
    _AVAILABLE_RECOGNIZERS = {"FREE": BarkRecognitionNoImplementation}

    @staticmethod
    def create_bark_recognizer(recognizer_type: str) -> BarkRecognitionInterface:
        """
        This function is used to create bark recognizer based on the subscription plan.
        All plans are stored in _AVAILABLE_RECOGNIZERS.

        :param recognizer_type: subscription plan

        :return: bark recognizer
        """
        try:
            return BarkRecognitionFactory._AVAILABLE_RECOGNIZERS[recognizer_type]()
        except KeyError:
            raise KeyError(f"There is no recognizer: {recognizer_type}")
