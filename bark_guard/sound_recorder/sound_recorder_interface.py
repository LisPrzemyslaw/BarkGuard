from abc import ABC, abstractmethod
import wavio


class SoundRecorderInterface(ABC):
    def __init__(self, frequency: int = 44100):
        self.frequency = frequency
        self.recorded_audio = None

    @abstractmethod
    def record(self, duration: float = 0) -> None:
        """
        This function should record audio for a given duration.

        :param duration: duration of the recording in seconds. If duration is 0, the recording should be continuous.
        """
        pass

    @abstractmethod
    def stop(self) -> None:
        """This function should stop the recording."""
        pass

    @abstractmethod
    def get_audio(self) -> bytes:
        """
        This function should return the recorded audio.

        :return: recorded audio
        """
        pass

    @abstractmethod
    def play_audio(self, audio: bytes) -> None:
        """
        This function should play the audio.
        :param audio:
        :return:
        """
        pass

    @abstractmethod
    def delete_audio(self) -> None:
        """This function should delete the recorded audio."""
        pass

    def get_audio_duration(self) -> float:
        """This function should return the duration of the recorded audio in seconds."""
        return len(self.recorded_audio) / self.frequency

    def save_audio(self, file_name: str) -> None:
        """
        This function should save the recorded audio to a file.

        :param file_name: name of the file without extension
        """
        wavio.write(f"{file_name}.wav", self.recorded_audio, self.frequency, sampwidth=2)
