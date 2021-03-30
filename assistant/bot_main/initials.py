import speech_recognition as sr
from bot_main.GUI import gui
import json


listener = sr.Recognizer()

information = json.loads(open('assistant/bot_main/assistant_info.json').read())

for info in information["assistant"]:
    name = info["name"]


def initials():
    global name

    try:
        with sr.Microphone() as source:
            gui.display("...")
            voice = listener.listen(source)
            recognise_name = listener.recognize_google(voice)
            recognise_name = recognise_name.lower()
                
    except Exception:
        recognise_name = 'none'
        #listener = sr.Recognizer()

    if name.lower() in recognise_name :
        return True

if __name__ == "__main__":
    print(initials())