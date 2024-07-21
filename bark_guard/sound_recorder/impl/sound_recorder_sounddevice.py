from bark_guard.sound_recorder.sound_recorder_interface import SoundRecorderInterface
import sounddevice


class SoundRecorderSoundDevice(SoundRecorderInterface):
    def __init__(self, frequency: int = 44100):
        super().__init__(frequency)

    def record(self, duration: float = 0) -> None:
        if duration == 0:
            raise NotImplementedError("Recording without duration is not implemented yet.")
        self.recorded_audio = sounddevice.rec(
            int(self.frequency * duration),
            samplerate=self.frequency,
            channels=1,
            dtype="int16",
        )
        sounddevice.wait()

    def stop(self) -> None:
        sounddevice.stop()

    def get_audio(self) -> bytes:
        return self.recorded_audio

    def play_audio(self, audio: bytes) -> None:
        raise NotImplementedError("Playing audio is not implemented yet.")

    def delete_audio(self) -> None:
        self.recorded_audio = None
        # TODO delete also from disc if exist
