class User:

    def __init__(self):
        self.__data = requests.get("htt")
        self.login = self.__data["Login"] if not log else log
        self.__password = ""
        self.imya = ""
        self.familiya = ""
        self.podpiski = []
        self.podpischiki = []

        print(self.__data)