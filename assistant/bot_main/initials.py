import speech_recognition as sr
from bot_main.GUI import gui
from configurations import theme


listener = sr.Recognizer()
name = theme.name


def initials():
    global name

    try:
        with sr.Microphone() as source:
            gui.display("...\n")
            voice = listener.listen(source)
            recognise_name = listener.recognize_google(voice)
            recognise_name = recognise_name.lower()

    except Exception:
        recognise_name = 'none'

    if name.lower() in recognise_name:
        return True


if __name__ == "__main__":
    print(initials())
