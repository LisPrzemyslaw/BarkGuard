from bark_guard.sound_recorder.sound_recorder_interface import SoundRecorderInterface
from bark_guard.sound_recorder.impl.sound_recorder_sounddevice import SoundRecorderSoundDevice
from enum import Enum, auto


class SoundRecorderType(Enum):
    SOUND_DEVICE = auto()


class SoundRecorderFactory:
    _AVAILABLE_SOUND_RECORDERS = {SoundRecorderType.SOUND_DEVICE: SoundRecorderSoundDevice}

    def create_sound_recorder(self, sound_recorder_type: SoundRecorderType) -> SoundRecorderInterface:
        try:
            return self._AVAILABLE_SOUND_RECORDERS[sound_recorder_type]()
        except KeyError:
            raise KeyError(f"There is no sound recorder: {sound_recorder_type}")
