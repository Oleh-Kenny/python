from random import randint


class Account:
    def __init__(self, card_number, amount, currancy):
        self.__card_number = card_number
        self.__amount = amount
        self.__currancy = currancy

    def ad_amount(self, ad_amount_money):
        self.__amount = self.__amount + ad_amount_money
        print("На ваш рахунок було додано: ", ad_amount_money, self.__currancy)
        input("Для продовження натисніть Enter")

    def take_amount(self, tk_amount):
        if self.__amount >= tk_amount:
            self.__amount = self.__amount - tk_amount
            print("Гроші з вашого рахунку були зняті: ",
                  tk_amount, self.__currancy)
            input("Для продовження натисніть Enter")
        else:
            print("Недостатньо коштів на рахунку\nНа вашому рахунку: ", self.__amount)
            input("Для продовження натисніть Enter")

    def show_info(self):
        print("Card namb: ", self.__card_number, "\nAmount: ",
              self.__amount, "\nCurrancy: ", self.__currancy)


while True:
    
    print("""
    Нажміть 1 для створення рахунку\n
    Нажміть 2 для поповнення вашого рахунку\n
    Нажміть 3 для зняття коштів\n
    Нажміть 4 для перевірки рахунку\n
    Натисніть 0 щоб вийти\n
    """)

    menu_chek = int(input())
    if menu_chek == 0:
        print("Не забудьте свою картку!!!")
        input()
        break

    elif menu_chek == 1:
        print("<< ---- Створення рахунку ---- >>")
        amount = int(input("Введіть кількість коштів: "))
        currancy = input("Виберіть валюту: UAH USD EUR \n--->")
        card_number = randint(000000000, 999999999)
        credit_card = Account(card_number, amount, currancy)

    elif menu_chek == 2:
        print("Скільки грошей буде покладено на рахунок?\n")
        plus_cash = int(input("Введiть суму: "))
        credit_card.ad_amount(plus_cash)

    elif menu_chek == 3:
        print("Скільки грошей буде знятo з рахунку?\n")
        take_cash = int(input("Введіть суму для зняття коштів: \n---> "))
        credit_card.take_amount(take_cash)

    elif menu_chek == 4:
        credit_card.show_info()
        print("\n")
