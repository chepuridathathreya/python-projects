#for playing music and opening websites and other stuff
import win32com.client as wincom
import musiclibrary
import speech_recognition as sr
import webbrowser
speaker = wincom.Dispatch("SAPI.SpVoice")


def speak(text):
    speaker.Speak(text)
    spvoice = speaker.GetVoices()
    speaker.Voice = spvoice.Item(1)
    speaker.rate = -1
    speaker.volume = 90

def processCommand(c):
    if "open youtube" in c.lower():
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        speak("opening facebook")
        webbrowser.open("https://www.facebook.com/")
    elif "open twitter" in c.lower():
        speak("opening twitter")
        webbrowser.open("https://www.twitter.com/")

    elif "play boy" or "playboy" in c.lower():
        speak("playing move")
        link = musiclibrary.song["boy"]     
        print(link)
        webbrowser.open(link)
if __name__ == "__main__":   
    speak("initializing matrix")     
    #when matrix is said do this
    while True:

        # obtain audio from the microphone
        

        # recognize speech using google 
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening..")
                audio = r.listen(source,
                                 timeout=2,
                                 phrase_time_limit=1)
                print("recognising")
            word = r.recognize_google(audio)
            print(word)
            word = word.lower().strip()
            if word == "hello" or word == "hi" or word == "jarvis":

                print("About to speak...")
                speak("yes sir")
                #listen to me
                with sr.Microphone() as source:

                    #print("activating matrix")
                    speak("activating matrix")
                    audio = r.listen(source )
                    #print("recognising")
                    command = r.recognize_google(audio)
                    #print(command)
                    processCommand(command)
                    print(command)



        except Exception as e:
            print("Error; {0}".format(e))
            