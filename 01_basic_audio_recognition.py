import speech_recognition as sr
import matplotlib.pyplot as plt
import wave
import numpy as np

recognizer=sr.Recognizer()
with sr.AudioFile("16-122828-0002.wav") as source:
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio)
    print("Recognized Text from the audio:")
    print(text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print("Speech recognition service error:", e)


with wave.open("16-122828-0002.wav", "rb") as wav:
    sample_rate = wav.getframerate()
    n_frames = wav.getnframes()
    audio_data = wav.readframes(n_frames)

samples = np.frombuffer(audio_data, dtype=np.int16)
time = np.arange(len(samples)) / sample_rate

plt.figure(figsize=(12, 4))
plt.plot(time, samples)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Speech Audio Waveform")
plt.grid()
plt.show()