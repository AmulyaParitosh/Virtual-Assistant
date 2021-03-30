from bot_main import processor
from main.text_to_speech import talk#
from main import initials#
from main import take_command
from main.word_game import WordGame
from main import tasks
import datetime
import wikipedia
from main.GUI import gui
import os



class Run_Assistant():

    def __init__(self):
    
        self.greet = True

        self.dictionary = tasks.Dictionary()
        self.question = tasks.Ask_question()
        self.open_in_browser = tasks.Open_in_browser()
        self.weather = tasks.Weather()
        self.news = tasks.News()
        self.maths = tasks.Mathparse()
        self.word_game = WordGame()

        pid = os.getpid()
        gui.display(pid)

    def close(self):

        hour = datetime.datetime.now().hour

        if hour>=21 or hour<=2:
            gui.display('\n'+"Good Night, Sleep Tight," +
                "\n Don't Let The Bed Bugs Bight")
            talk("Good night sleep tight, don't let the bed bugs bight")
            gui.stop()
            exit()                      # closes perform_task

        elif hour > 2 and hour < 4:
            gui.display('\n Abee soo jaa BSDK')
            talk('Abee so jaa B S D K') 
            gui.stop() 
            exit()                      # closes perform_task

        else:
            gui.display('\n'+'See you later, Alligator')
            talk('See you later, Alligator')
            gui.stop()
            exit()                      # closes perform_task

    def greatings(self):

        hour = datetime.datetime.now().hour
        if hour>=0 and hour<12:
            gui.display('\n'+"Hello,Good Morning\n")
            talk("Hello, Good Morning")
            talk("How may I help you?")
            
        elif hour>=12 and hour<16:
            gui.display('\n'+"Hello,Good Afternoon\n")
            talk("Hello, Good Afternoon")
            talk("How may I help you?")
            
        else:
            gui.display("Hello,Good Evening\n")
            talk("Hello, Good Evening")
            talk("How may I help you?")

    def get_task(self):
        message = take_command.command()

        if 'none' not in message:
            
            ints = processor.predict_class(message)
            action = processor.get_action(ints)
            res = processor.get_response(ints)
            
            if action == "chat":            
                return "response", res

            elif action == "task":            
                return res, message

            else:
                return "none", "none"
        else:
            return "none", "none"

    def perform_task(self):

        typ,command = self.get_task()
        
        if typ == "response":#
            gui.display(command)
            talk(command)

        elif typ == "close":#
            self.close()

        elif typ == 'time':#
            time = datetime.datetime.now().strftime('%I:%M:%p')
            gui.display('\n'+time)
            talk('the time is ' + time.replace(':', '') )

        elif typ == "wikisearch":#
            wikisearch = command.replace('who is', '')
            info = wikipedia.summary(wikisearch,2)
            gui.display('\n'+info)
            talk(info)

        elif typ == "meaning":#
            self.dictionary.meaning(command)

        elif typ == "antonym":#
            self.dictionary.antonym(command)       

        elif typ == "synonym":#
            self.dictionary.synonym(command)
            
        elif typ == "wolframalpha":#
            self.question.question()
            
        elif typ == "url":#
            self.open_in_browser.open_url(command)

        elif typ == "open site":#
            self.open_in_browser.open_special(command)

        elif typ == "youtube":#
            self.open_in_browser.play_in_yt(command)

        elif typ == "weather":#
            self.weather.get_weather()

        elif typ == "maths":#
            self.maths.solve(command)

        elif typ == 'news':#
            self.news.get_news()

        elif typ == 'word_game':
            self.word_game.play()

        elif typ == "none":
            gui.display('\n'+'sorry I did not get you')
            talk('sorry I did not get you')

    def RUN(self):

        while True:

            while initials.initials():

                talk('yes sir')
                if self.greet:
                    self.greatings()
                    self.greet = False
                self.perform_task()

assistant = Run_Assistant()
try:
    assistant.RUN()

except Exception:
    print("An error occored")
    assistant.RUN()