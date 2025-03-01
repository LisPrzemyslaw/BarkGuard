import os

from bark_guard.sound_recorder.impl.sound_recorder_sounddevice import SoundRecorderSoundDevice
from collections import deque
from matplotlib import pyplot as plt
import pprint

import numpy as np
import librosa

"""
Cechy:
TODO
"""


def get_limited_fft(sound: np.ndarray, sr: int | float) -> tuple[np.ndarray, np.ndarray]:
    """
    This function calculates the FFT spectrum of the sound.

    :param sound: recorded sound
    :param sr: sample rate

    :return: two numpy arrays fft_spectrum and frequencies
    """
    fft_spectrum = np.abs(np.fft.rfft(sound))  # Amplitude
    frequencies = np.fft.rfftfreq(len(sound), 1 / sr)

    thousand_freq_index = np.searchsorted(frequencies, 1000)

    if len(frequencies) != len(fft_spectrum):
        raise ValueError("Length of frequencies and fft_spectrum must be equal.")

    fft_spectrum = fft_spectrum[:thousand_freq_index]
    frequencies = frequencies[:thousand_freq_index]

    return fft_spectrum, frequencies


folder_path = r"D:\startup_by_me\BarkGuard\sample_data"
# files = os.listdir(folder_path)
# files = [file for file in files if file.endswith(".wav")]
# results = {}
# for file in files:
#     original_sound, sr = librosa.load(os.path.join(folder_path, file), sr=None)
#
#     fft_spectrum, frequencies = get_limited_fft(original_sound, sr)
#
#     if max(fft_spectrum) > 600:
#         results[file] = True
#     else:
#         results[file] = False
# pprint.pprint(results)


original_sound, sr = librosa.load(os.path.join(folder_path, "single_bark_1.wav"), sr=None)
fft_spectrum, frequencies = get_limited_fft(original_sound, sr)

# Wykresy
plt.figure(figsize=(10, 8))

# 3. Widmo po FFT
# plt.subplot(3, 1, 2)
plt.plot(frequencies, fft_spectrum, label="Widmo (FFT)")
plt.legend()
plt.xlabel("Częstotliwość (Hz)")
plt.ylabel("Amplituda")

# # 1. Oryginalny sygnał
# plt.subplot(3, 1, 1)
# plt.plot(y, label="Oryginalny dźwięk")
# plt.legend()
# plt.xlabel("Próbki")
# plt.ylabel("Amplituda")
# plt.subplot(3, 1, 3)
# plt.hist(y, bins=50, color='g', alpha=0.7, label="Histogram amplitud")
# plt.legend()
# plt.xlabel("Amplituda")
# plt.ylabel("Liczba próbek")
#
plt.tight_layout()
plt.show()
