from __future__ import annotations

from typing import TYPE_CHECKING

from bark_guard_client.sound_recorder.sound_recorder_interface import SoundRecorderInterface
import sounddevice

if TYPE_CHECKING:
    from collections import deque


class SoundRecorderSoundDevice(SoundRecorderInterface):
    def __init__(self, audio_container: deque, frequency: int = 44100):
        """
        :param audio_container: container for recorded audio
        :param frequency: frequency of the audio recording
        """
        super().__init__(audio_container, frequency)

    def _record_audio_in_thread(self, period_duration: float = 0) -> None:
        if period_duration == 0:
            raise NotImplementedError("Recording without duration is not implemented yet.")
        while not self._is_stop:
            recorded_audio = sounddevice.rec(
                int(self.frequency * period_duration),
                samplerate=self.frequency,
                channels=1,
                dtype="int16",
            )
            sounddevice.wait()
            self.audio_container.append(recorded_audio)

    def stop(self) -> None:
        super().stop()
        sounddevice.stop()

    def save_audio(self, file_name: str, recorded_audio) -> None:
        """
        This function should save the recorded audio to a file.

        :param file_name: name of the file without extension
        :param recorded_audio: audio to save, usually with barking sounds
        """
        raise NotImplementedError("Saving audio is not implemented yet.")
