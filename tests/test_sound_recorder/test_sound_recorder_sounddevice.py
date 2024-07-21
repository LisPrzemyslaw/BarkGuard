import pytest
from bark_guard.sound_recorder.impl.sound_recorder_sounddevice import SoundRecorderSoundDevice


class Test:
    def test_create_sound_recorder(self):
        """This test verifies that the SoundRecorderSoundDevice class can be created."""
        sound_recorder = SoundRecorderSoundDevice()
        assert sound_recorder is not None
        assert sound_recorder.frequency == 44100
        assert sound_recorder.recorded_audio is None

    @pytest.mark.skip(reason="Recording is not possible in github actions.")
    def test_record(self):
        """This test verifies that the record function works correctly."""
        sound_recorder = SoundRecorderSoundDevice()
        sound_recorder.record(1)
        assert sound_recorder.recorded_audio is not None
        assert len(sound_recorder.recorded_audio) == 44100
        assert sound_recorder.get_audio_duration() == 1
