from collections import deque
from bark_guard.sound_recorder.sound_recorder_factory import SoundRecorderFactory, SoundRecorderType

FREQUENCY = 44100


def main():
    audio_container = deque()
    sound_recorder = SoundRecorderFactory.create_sound_recorder(SoundRecorderType.SOUND_DEVICE, audio_container, FREQUENCY)

    sound_recorder.record(3)
    ...
    sound_recorder.stop()


if __name__ == "__main__":
    main()
