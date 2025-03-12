from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections import deque

from bark_guard_client.sound_recorder.sound_recorder_interface import SoundRecorderInterface
from bark_guard_client.sound_recorder.impl.sound_recorder_sounddevice import SoundRecorderSoundDevice
from enum import Enum, auto


class SoundRecorderType(Enum):
    SOUND_DEVICE = auto()


class SoundRecorderFactory:
    _AVAILABLE_SOUND_RECORDERS = {SoundRecorderType.SOUND_DEVICE: SoundRecorderSoundDevice}

    @staticmethod
    def create_sound_recorder(
            sound_recorder_type: SoundRecorderType,
            audio_container: deque,
            frequency: int = 44100
    ) -> SoundRecorderInterface:
        try:
            return SoundRecorderFactory._AVAILABLE_SOUND_RECORDERS[sound_recorder_type](audio_container, frequency)
        except KeyError:
            raise KeyError(f"There is no sound recorder: {sound_recorder_type}")
