from random_word import RandomWords
import time
from take_command import command#
from GUI import gui#
from text_to_speech import talk#
from PyDictionary import PyDictionary

dic = PyDictionary()
rw = RandomWords()

play = True
compwords = []
playerwords = []

def check_word(word):
    return (dic.meaning(word) != None)



while play:
    
    compword = rw.get_random_word(hasDictionaryDef="true")
    compwords.append(compword)
    gui.display(compword)
    talk(compword)

    reply = command()  

    if reply != 'none':

        if dic.meaning(reply) != None:

            if compword[-1] == reply[0]:

                if reply not in playerwords and reply not in compwords:
                    playerwords.append(reply)

                else:
                    gui.display("you used that word already")
                    talk("you used that word already")
                    gui.display("you loose")
                    talk("you loose")
                    play = False

            else:
                gui.display("Against the rule, you loose")
                talk("Against the rule, you loose")

        else:
            gui.display("Not a Real Word, You loose")
            talk("Not a Real Word, You loose")

    else:
        gui.display('Too late!! You loose')
        talk("too late, you loose")

        play = False

else:
    exit(0)
