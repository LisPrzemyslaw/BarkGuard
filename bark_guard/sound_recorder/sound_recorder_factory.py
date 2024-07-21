from bark_guard.sound_recorder.sound_recorder_interface import SoundRecorderInterface


class SoundRecorderFactory:
    _AVAILABLE_SOUND_RECORDERS = {}

    def create_sound_recorder(self, sound_recorder_type: SoundRecorderInterface) -> SoundRecorderInterface:
        try:
            return self._AVAILABLE_SOUND_RECORDERS[sound_recorder_type]()
        except KeyError:
            raise KeyError(f"There is no sound recorder: {sound_recorder_type}")
