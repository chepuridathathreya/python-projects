import pyttsx3
engine = pyttsx3.init(driverName='sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
print(voice[1].id)

print("Welcome to RoboSpeaker")
while True:
    x = input("Enter a command for the RoboSpeaker: ")

    if x == "bb":
        print("Exiting RoboSpeaker")
        engine.say("Exiting RoboSpeaker")
        engine.runAndWait()
        break

    engine.say(x)
    engine.runAndWait()