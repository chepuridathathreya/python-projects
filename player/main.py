#tried pyttsx3 and speech recognition for voice commands and responses, but it is not working as expected. I will try to fix it later.
import pyttsx3
import speech_recognition as sr
import webbrowser

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":   
    speak("initializing jarvis")     
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
