import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
spvoice = speak.GetVoices()
speak.Voice = spvoice.Item(1)
speak.rate = -1
speak.volume = 90

while True:

    text = input("enter what u want to make the robo to speak : ")
    if text == "close":
        speak.Speak("exiting robo speaker")
        break

    speak.Speak(text)
