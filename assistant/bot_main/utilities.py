from bot_main.text_to_speech import talk
from bot_main.GUI import gui
from bot_main.take_command import command
import nltk
from PyDictionary import PyDictionary
from pyNewsApi import PYNEWS
import requests
import webbrowser
import validators
import json
import wolframalpha
from mathparse import mathparse
from random_word import RandomWords
import time


def get_stem(sentence, de_word: list):
    wr_list = nltk.word_tokenize(sentence.lower())
    stem = ""
    for w in de_word:
        if w in wr_list:
            wr_list.remove(w)

    for e in wr_list:
        stem += e+" "

    return stem[:-1]


class Dictionary():

    def __init__(self):
        self.dictionary = PyDictionary()

    def meaning(self, text):

        de_word = ["what", 'is', 'are', 'the', 'meanings',
                   'meaning', 'of', "a", "?", ".", ","]
        word = get_stem(text, de_word)

        meaning = self.dictionary.meaning(word)
        gui.display(word.upper()+':--')
        talk('meanings of '+word+' are ')
        key = list(meaning)
        for i in range(len(meaning)):
            gui.display(key[i]+' -')
            talk('as a '+key[i])
            v = meaning[key[i]]
            for e in range(len(v)):
                gui.display('\n'+str(e+1)+') '+v[e])
                talk(v[e])

            gui.display('\n')

    def antonym(self, text):
        de_word = ["what", 'is', 'are', 'the', 'antonyms',
                   'antonym', 'of', "a", "?", ".", ","]
        word = get_stem(text, de_word)

        antonym = self.dictionary.antonym(word)
        gui.display(word.upper()+':--')
        talk('antonyms of '+word+' are ')
        for i in range(len(antonym)):
            gui.display(str(i+1)+') '+antonym[i])
            talk(antonym[i])

    def synonym(self, text):
        de_word = ["what", 'is', 'are', 'the', 'synonyms',
                   'synonym', 'of', "a", "?", ".", ","]
        word = get_stem(text, de_word)

        synonym = self.dictionary.synonym(word)
        gui.display(word.upper()+':--')
        talk('synonyms of '+word+' are ')
        for i in range(len(synonym)):
            gui.display(str(i+1)+') '+synonym[i])
            talk(synonym[i])


class News():

    def __init__(self):

        pynews = PYNEWS()
        self.news = pynews.get_headlines_by_country('in')
        self.lit = list()

    def headlines(self, x, y):

        for i in range(x, y):
            headlines = (self.news[i])['title']
            gui.display('\n' + headlines)
            talk(headlines)
            headlines = headlines.lower()
            self.lit.append(headlines)

    def details(self, text):

        if 'exit' not in text:
            topic = text.replace('tell me more about ', '')
            for i in range(len(self.lit)):
                if topic in self.lit[i]:
                    description = (self.news[i])['description']
                    gui.display(description)
                    talk(description)

                    gui.display('do you want more details?')
                    talk('do you want more details?')
                    reply = command()
                    if 'tell me more about' in reply:
                        self.details(reply)

                    elif 'no' in reply:
                        gui.display("that's all for current news headlines")
                        talk("that's all for current news headlines")

                    else:
                        gui.display('sorry I did not get you')
                        talk('sorry I did not get you')
                        gui.display('please repeat')
                        talk('please repeat')
                        reply = command()
                        self.details(reply)

                else:
                    if i+1 == len(self.lit):
                        gui.display('sorry I did not get you')
                        talk('sorry I did not get you')
                        gui.display('please repeat')
                        talk('please repeat')
                        reply = command()
                        self.details(reply)

    def get_news(self):

        gui.display("today's news headlines are :")
        talk("today's news headlines are")

        self.headlines(0, 5)

        gui.display('do you want more news headlines?')
        talk('do you want more headlines?')
        reply = command()

        if 'yes' in reply:
            self.headlines(5, 10)
            gui.display('do you want more details?')
            talk('do you want more details?')
            reply = command()

            if 'tell me more about' in reply:
                self.details(reply)
                gui.display("that's all for current news headlines")
                talk("that's all for current news headlines")

            else:
                gui.display("that's all for current news headlines")
                talk("that's all for current news headlines")

        elif 'tell me more about' in reply:
            self.details(reply)
            gui.display("that's all for current news headlines")
            talk("that's all for current news headlines")

        else:
            gui.display("that's all for current news headlines")
            talk("that's all for current news headlines")


class Open_in_browser():

    def play_in_yt(self, topic):

        de_word = ["open", "in", 'youtube', 'play', 'on', 'play_yt', '_yt']
        topic = get_stem(topic, de_word)

        url = 'https://www.youtube.com/results?q=' + topic
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == 'WEB_PAGE_TYPE_WATCH':
                break
        if lst[count-5] == "/results":
            raise Exception("No video found.")

        #print("Videos found, opening most recent video")
        webbrowser.open("https://www.youtube.com"+lst[count-5])

        talk('playing' + topic)
        gui.display(f"playing {topic}")

    def validator(self, url):
        validity = validators.url(url)
        return validity

    def open_url(self, topic):

        de_word = ['open', 'the', 'site', 'url']
        topic = get_stem(topic, de_word)
        url = 'https://'+topic

        if self.validator(url):
            gui.display('\n'+url)
            webbrowser.open(url)
            de_word = ['https://', 'www.', '.com', '.in']
            for w in de_word:
                if w in url:
                    url = url.replace(w, '')
            talk('opening '+url)
        else:
            gui.display('\nSorry!  Invalid url!')
            talk('Sorry! Invalid u r l')

    def open_special(self, topic):

        de_word = ['open']
        site = get_stem(topic, de_word)

        if 'amazon' in site:
            url = 'https://www.amazon.in/'
            webbrowser.open(url)
            gui.display('\n'+url)
            talk('opening'+site)

        if 'google' in site:
            url = 'https://www.google.com/'
            webbrowser.open(url)
            gui.display('\n'+url)
            talk('opening'+site)

        if 'facebook' in site:
            url = 'https://www.facebook.com/'
            webbrowser.open(url)
            gui.display('\n'+url)
            talk('opening'+site)

        if 'facebook' in site:
            url = 'https://www.facebook.com/'
            webbrowser.open(url)
            gui.display('\n'+url)
            talk('opening'+site)

        if 'reddit' in site:
            url = 'https://www.reddit.com/'
            webbrowser.open(url)
            gui.display('\n'+url)
            talk('opening'+site)

        if 'github' in site:
            url = 'https://www.github.com/'
            webbrowser.open(url)
            gui.display('\n'+url)
            talk('opening'+site)

        else:
            gui.display('\nSorry! I am currently limited in my capablities')
            talk('Sorry! I am currently limited in my capablities')


class Weather():

    def __init__(self):

        api_key = "b3a5bb5e544a18b276677b286784fc5d"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        city_name = "Ranchi, IN"
        self.complete_url = base_url+"appid="+api_key+"&q="+city_name

    def get_weather(self):
        response = requests.get(self.complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = int(y["temp"] - 273)
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]

            gui.display('\nWEATHER REPORT -')
            talk('current weather report is as follows')

            gui.display(" Temperature = " + str(current_temperature) + "°С" +
                        "\n Humidity = " + str(current_humidiy) + "(%)" +
                        "\n Description = " + str(weather_description) + '\n')

            talk("Temperature is " + str(current_temperature) + "degree celcius" +
                 "\n Humidity is " + str(current_humidiy) + " percent"
                 "\n and, it is " + str(weather_description))


class Ask_question():
    def __init__(self):

        app_id = "J89VAX-7U7HU8UTRQ"
        self.clint = wolframalpha.Client(app_id)

    def question(self):
        gui.display('\n please, let me help you')
        talk('please, let me help you')

        question = command()

        res = self.clint.query(question)

        answer = next(res.results).text

        gui.display('\n'+answer)
        talk(answer)


class Mathparse():

    def solve(self, statement):

        de_word = ['mathparse']
        statement = get_stem(statement, de_word)

        statement = statement.replace("to the power", "^")
        statement = statement.replace("into", "*")
        statement = statement.replace("multiplied by", "*")
        statement = statement.replace("divided by", "/")
        statement = statement.replace("by", "/")

        expression = mathparse.extract_expression(statement, language='ENG')
        ans = mathparse.parse(expression)

        gui.display(f"{expression} = {ans}")
        talk(f"{expression} = {ans}")


class WordGame:

    def __init__(self):

        self.dic = PyDictionary()
        self.rw = RandomWords()

        self.playing = True
        self.compwords = []
        self.playerwords = []

    def play(self):

        gui.display("Wellcome to Word Game. Let's play")
        talk("Wellcome to Word Game. Let's play")

        while self.playing:

            compword = self.rw.get_random_word(hasDictionaryDef="true")
            self.compwords.append(compword)
            gui.display(compword)
            talk(compword)

            reply = command()

            if reply != 'none':

                if self.dic.meaning(reply) != None:

                    if compword[-1] == reply[0]:

                        if reply not in self.playerwords and reply not in self.compwords:
                            self.playerwords.append(reply)

                        else:
                            gui.display("you used that word already")
                            talk("you used that word already")
                            gui.display("you loose")
                            talk("you loose")
                            self.playing = False

                    else:
                        gui.display("Against the rule, you loose")
                        talk("Against the rule, you loose")
                        self.playing = False

                else:
                    gui.display("Not a Real Word, You loose")
                    talk("Not a Real Word, You loose")
                    self.playing = False

            else:
                gui.display('Too late!! You loose')
                talk("too late, you loose")
                self.playing = False
