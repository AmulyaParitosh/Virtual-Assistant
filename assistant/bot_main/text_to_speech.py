import pyttsx3
# from configurations import theme


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


# engine.setProperty('voice', voices[names[theme.voice]].id)
engine.setProperty('voice', 'english')

engine.setProperty('rate', 150)


def talk(text):

    engine.say(text)
    engine.runAndWait()
    return


def voices_in_system():

    converter = pyttsx3.init()
    voices = converter.getProperty('voices')

    for voice in voices:
        # to get the info. about various voices in our PC
        with open("assistant/bot_main/voices.txt", 'w') as file:
            file.write("Vices:")
            for voice in voices:
                file.write("ID: %s\n" % voice.id)
                file.write("Name: %s\n" % voice.name)
                file.write("Age: %s\n" % voice.age)
                file.write("Gender: %s\n" % voice.gender)
                file.write("Languages Known: %s\n" % voice.languages)
                file.write("\n")


if __name__ == "__main__":
    talk("hi, How are you?")
    talk("all good")
    # voices_in_system()
