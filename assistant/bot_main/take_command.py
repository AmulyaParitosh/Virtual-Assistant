import speech_recognition as sr
from bot_main.GUI import gui
from configurations import theme

listener = sr.Recognizer()
name = theme.name


def command():

    try:
        with sr.Microphone() as source:
            gui.display('\tlistening...\n')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

    except:
        command = 'none'

    gui.display('->> ' + command + '\n')
    return command


def simple_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

    except:
        command = 'none'

    print('\ncommand : ' + command + '\n')
    return command


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
