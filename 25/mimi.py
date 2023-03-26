# class Anton:
#     location = "Новосибирск"
#     def __init__(self, rost=56, ves=135):
#         self.height = rost
#         self.wright = ves
#         self.otkuda = Anton.location
#
#         def __private(self):
#             pass
#
#         def __private(self):
#             pass
#
# chelovek = Anton(10)
# chelovek2 = Anton(57)
# print(chelovek.height)

class Human:
    default_name = "House"

    def __init__(self,default_name, default_age):
        self.name = default_name
        self.age = default_age
        self.__money = 1
        self.__house= None

    def __make_deal(self,dom):
         if self.__money >= dom.final_price():
             self.__money -= dom.final_price()
             return True
         else:
             return False

    def buy_house(self, dom):
         if self.__make_deal(dom):
             dom.owner= self.name
             self.__house = dom
             return "купил "

class House():
    def __init__(self):
        self.__price = 5000

    def final_price(self):
        return self.__price - 500


artem = Human("Глеб", 5)
dom1 = House()

print(artem.buy_house(dom1))

