import speech_recognition as sr
recognizer=sr.Recognizer()
with sr.AudioFile("16-122828-0002.wav") as source:
    print("Audio source:", source)
    print("Sample rate:", source.SAMPLE_RATE) #in hertz (Hz)
    print("Sample width:", source.SAMPLE_WIDTH) #in bytes
    audio = recognizer.record(source)

print("Audio duration:", len(audio.frame_data) / (source.SAMPLE_RATE * source.SAMPLE_WIDTH))

try:
    text = recognizer.recognize_google(audio)
    print("Recognized Text:", text)
except sr.UnknownValueError:
    print("Could not understand the audio.")
except sr.RequestError as e:
    print("Service error:", e)