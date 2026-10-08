import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("16-122828-0002.wav") as source:
    audio = recognizer.record(source)

try:
    print("Google:")
    print(recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Google could not understand the audio.")
except sr.RequestError:
    print("Google service unavailable.")

