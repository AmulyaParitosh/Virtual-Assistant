import speech_recognition as sr
from GUI import gui
import json


listener = sr.Recognizer()

information = json.loads(open('assistant_info.json').read())

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
                
    except:
        recognise_name = 'none'

    if name.lower() in recognise_name :
        return True

