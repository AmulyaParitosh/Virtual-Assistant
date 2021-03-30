from random_word import RandomWords
import time
from main.take_command import command#
from main.GUI import gui#
from main.text_to_speech import talk#
from PyDictionary import PyDictionary


dic = PyDictionary()
rw = RandomWords()

class WordGame:

    def __init__(self):

        self.playing = True
        self.compwords = []
        self.playerwords = []


    def play(self):

        gui.display("Wellcome to Word Game. Let's play")
        talk("Wellcome to Word Game. Let's play")

        while self.playing:
            
            compword = rw.get_random_word(hasDictionaryDef="true")
            self.compwords.append(compword)
            gui.display(compword)
            talk(compword)

            reply = command()  

            if reply != 'none':

                if dic.meaning(reply) != None:

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


if __name__ == "__main__":
    wordgame = WordGame()
    wordgame.play()