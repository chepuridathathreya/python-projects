import pyttsx3

engine = pyttsx3.init()

print("Welcome to RoboSpeaker")

while True:
    
    engine = pyttsx3.init()
    x = input("Enter a command for the RoboSpeaker: ")
    print("robo speaking...")

    if x == "bb":
        print("Exiting RoboSpeaker")
        engine.say("Exiting RoboSpeaker")
        engine.runAndWait()
        engine.stop()
        
        break
    engine.say(x)
    engine.runAndWait()
    
    print("robo done speaking...")
    