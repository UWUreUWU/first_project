
import playsound

class MusicBox:

        def __init__(self):
            self.__variants = "OFRZ"
            self.__score = 0
            self.__sequence = choice(self.__variants)


    def get_score(self):
            print(self.__sequence)

        def play(self):
           for bukva in self.__sequence:
            playsound.playsound(f"sounds/{bukva}.mp3")

            def check(self, predpolojenie):
                playsound.playsound("sounds/correct.wav")
            self.__score += 1


            def __next(self):
                self.__sequence += choice(self.__variants)