import pyttsx3
engine = pyttsx3.init(driverName='sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)
print(voice[0].id)