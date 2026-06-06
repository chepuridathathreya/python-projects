import os
if __name__=="__main__":
    print("welcome to the robospeaker")
    while True:
        x = input("Enter a command for the robospeaker : ") 
        if x == "bb":
            os.system("say 'exiting the robo'")
            break
        command = f'powershell -c "Add-Type -AssemblyName System.Speech; ' \
                    f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
        
        os.system(command)
        