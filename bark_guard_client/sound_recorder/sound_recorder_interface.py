from __future__ import annotations

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod
import threading

if TYPE_CHECKING:
    from collections import deque


class SoundRecorderInterface(ABC):
    def __init__(self, audio_container: deque, frequency: int = 44100):
        """
        This class should be used as an interface for all sound recorders.

        :param audio_container: container for recorded audio
        :param frequency: frequency of the audio recording
        """
        self.audio_container: deque = audio_container
        self.frequency: int = frequency

        self.thread: threading.Thread | None = None
        self._is_stop = False

    def record(self, period_duration: float = 0) -> None:
        """
        This function should record audio continuously in a given periods of times.

        :param period_duration: duration of the recording in seconds. If duration is 0, the recording should be continuous.
        """
        self.thread = threading.Thread(target=self._record_audio_in_thread, args=(period_duration,), daemon=True)
        self.thread.start()

    def stop(self) -> None:
        """This function should stop the recording thread by changing the flag."""
        self._is_stop = True
        self.thread.join()

    @abstractmethod
    def _record_audio_in_thread(self, period_duration: float = 0) -> None:
        """
        This function should record audio in a separate thread.

        :param period_duration: duration of the recording in seconds. If duration is 0, the recording should be continuous.
        """
        pass

    @abstractmethod
    def save_audio(self, file_name: str, recorded_audio) -> None:
        """
        This function should save the recorded audio to a file.

        :param file_name: name of the file without extension
        :param recorded_audio: audio to save, usually with barking sounds
        """
        pass
