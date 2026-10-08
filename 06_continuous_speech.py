import speech_recognition as sr

recognizer = sr.Recognizer()
microphone = sr.Microphone()

with microphone as source:
    print("Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Live speech recognition started.")
    print("Press Ctrl+C to stop.")

    while True:
        try:
            print("\nListening...")
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("Text:", text)
        except sr.UnknownValueError:
            print("Could not understand.")
        except sr.RequestError as e:
            print("Service error:", e)
        except KeyboardInterrupt:
            print("\nStopped.")
            break