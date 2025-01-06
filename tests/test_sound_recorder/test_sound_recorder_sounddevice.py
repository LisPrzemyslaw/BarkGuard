from collections import deque
import pytest
from bark_guard.sound_recorder.impl.sound_recorder_sounddevice import SoundRecorderSoundDevice


class Test:
    def test_create_sound_recorder(self):
        """This test verifies that the SoundRecorderSoundDevice class can be created."""
        # Condition
        audio_container = deque()
        frequency = 44100
        # Action
        sound_recorder = SoundRecorderSoundDevice(audio_container, frequency)
        # Expectation
        assert sound_recorder is not None
        assert sound_recorder.frequency == frequency
        assert sound_recorder._is_stop is False
        assert sound_recorder.thread is None
        assert sound_recorder.audio_container == audio_container

    @pytest.mark.skip(reason="Recording is not possible in github actions.")
    def test_record(self):
        """This test verifies that the record function works correctly."""
        # Condition
        audio_container = deque()
        frequency = 44100
        # Action
        sound_recorder = SoundRecorderSoundDevice(audio_container, frequency)
        sound_recorder.record(1)
        sound_recorder.stop()
        # Expectation
        assert isinstance(sound_recorder.audio_container, deque)
        assert len(sound_recorder.audio_container) == 1
        assert len(sound_recorder.audio_container[0]) == 44100
