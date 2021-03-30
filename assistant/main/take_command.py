import speech_recognition as sr
from main.GUI import gui#

listener = sr.Recognizer()


def command():
       
    try:
        with sr.Microphone() as source:
            gui.display('listening...\n')
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