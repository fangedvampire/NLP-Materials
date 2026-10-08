import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1) #1 second adjustment
    print("Start speaking...")

    audio = recognizer.listen(source, timeout=5, phrase_time_limit=10) #timeout after 5 seconds of silence, limit to 10 seconds of speech

try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Could not understand your speech.")
except sr.RequestError as e:
    print("Service error:", e)