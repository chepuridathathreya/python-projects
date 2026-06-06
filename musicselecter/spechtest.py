
import speech_recognition as sr




for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Index {index}: {name}")

  

def recognize_speech():
    # Initialize the recognizer
    r = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening...")
        # Capture the audio from the microphone
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Use Google's free Web Speech API to recognize the audio
        text = r.recognize_amazon(audio)
        print(f"You said: {text}")
        
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from the service; {e}")

if __name__ == "__main__":
    recognize_speech()


