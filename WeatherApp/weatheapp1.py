import json
import requests 
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
spvoice = speak.GetVoices()
speak.Voice = spvoice.Item(0)
speak.rate = -1
speak.volume = 90
while True:
    city = input("enter the city name : ")
    if city == "close":
        speak.Speak("exiting weather app")
        break
    url = f"http://api.weatherapi.com/v1/current.json?key=744fe5f7e4a64a46b6881413261805&q={city}"
    output = requests.get(url)
    #print(output.text)
    wetdic=json.loads(output.text)
    temp=wetdic ["current"]["temp_c"]
    humid=wetdic["current"]["humidity"]
    #temp=str(temp)
    #print(type(temp))
    print('speaking...')
    print(f"the current temperature in {city} is {temp} degree celsius and humidity is {humid} percent")
    result=speak.Speak(f"the current temperature in {city} is {temp} degree celsius and humidity is {humid} percent")
    print(result)
     