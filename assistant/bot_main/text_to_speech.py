import pyttsx3
from configurations import theme


engine = pyttsx3.init()
voices = engine.getProperty('voices')
names = {
    'David': 0,
    'Heera': 1,
    'Ravi': 2,
    'Mark': 3,
    'Cortana': 4,
    'Zira': 5
}


engine.setProperty('voice', voices[names[theme.voice]].id)
engine.setProperty('rate', 220)


def talk(text):

    engine.say(text)
    engine.runAndWait()
    return


def voices_in_system():

    converter = pyttsx3.init()
    voices = converter.getProperty('voices')

    for voice in voices:
        # to get the info. about various voices in our PC
        print("Voice:")
        print("ID: %s" % voice.id)
        print("Name: %s" % voice.name)
        print("Age: %s" % voice.age)
        print("Gender: %s" % voice.gender)
        print("Languages Known: %s" % voice.languages)


if __name__ == "__main__":
    talk("hiii")
    talk("all good")
    voices_in_system()
