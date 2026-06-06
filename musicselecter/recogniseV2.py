#included notes and date and time and calculator and notepad
import win32com.client as wincom
import speech_recognition as sr
import webbrowser
import datetime
import os
import musiclibrary
speaker = wincom.Dispatch("SAPI.SpVoice")

def speak(text):
    spvoice = speaker.GetVoices()
    speaker.Voice = spvoice.Item(1)
    speaker.rate = -1
    speaker.volume = 90
    speaker.Speak(text)

def take_note():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening..")
        audio = r.listen(source,
                         timeout=2,
                         phrase_time_limit=8)
        print("recognising")
    note = r.recognize_google(audio)
    print(note)
    with open("musicselecter/notes.txt", "a") as file:
        print("Note added!")
        file.write(note + "\n")    
def show_notes():
    with open("musicselecter/notes.txt", "r") as readfile:
        print("you have written:")
        print(readfile.read())
# def clear_notes():
#     with open("fileproject/nfile.txt", "w") as file:
#         print("Notes cleared!")
# def count_notes():
#     with open("fileproject/nfile.txt", "r") as readnotes:
#         notes = readnotes.readlines()
#         print(f"You have {len(notes)} notes.")
              
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
    #elif "play boy" or "playboy" in c.lower():
    #    speak("playing move")
     #   link = musiclibrary.song["boy"]     
      #  print(link)
       # webbrowser.open(link)
    elif "tell time" in c.lower() or "time" in c.lower():
        current_time = datetime.datetime.now().strftime("%H:%M")
        print(f"Current time is : {current_time}")
        speak(f"Current time is : {current_time}")
    elif "tell me " in c.lower() or "date" in c.lower():
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Current date is : {current_date}")
        speak(f"Current date is : {current_date}")
    elif "open calculator" in c.lower() or "calculator" in c.lower():
        speak("opening calculator")  
        os.system("calc.exe")          
    elif "open notepad" in c.lower() or "notepad" in c.lower():
        speak("opening notepad")  
        os.system("notepad.exe")  
    elif "take note" in c.lower() or "text" in c.lower():
        speak("what do you want to note?")
        take_note()
    elif "show notes" in c.lower() or "notes" in c.lower():
        speak("showing notes")
        show_notes()          


if __name__ == "__main__":   
    speak("initializing matrix")     
    #when matrix is said do this
    while True:

        # obtain audio from the microphone
        

        # recognize speech using google 
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=1)
                print("listening..")
                audio = r.listen(source,timeout=2, phrase_time_limit=1)
                print("recognising")
            word = r.recognize_google(audio)
            print(word)
            word = word.lower().strip()
            if word in ["hello", "hi", "jarvis", "matrix"]:

                print("About to speak...")
                print("yes sir!!")
                speak("yes sir")
                #listen to me
                with sr.Microphone() as source:
                    print("listening..")
                    audio = r.listen(source,
                                     timeout=2,
                                     phrase_time_limit=1)
                    print("recognising")
                    command = r.recognize_google(audio)
                    print(command)                    
                    processCommand(command)
                    

        except Exception as e:
            print("Error; {0}".format(e))                
