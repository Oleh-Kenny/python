############### DZ ################


# ==================================================== #
# пора дня від введеного часу

# a = int(input("Введіть час: "))
# if a <= 6:
#  print("Ніч")
# elif a <= 12:
# print("РАнок")
# elif a <= 18:
# print ("День")
# elif a <= 24:
# print("Ввечір")
# else :
#  print("errror")


# ==================================================== #
###КОНВЕНТР###


# dlina = int(input(' 1. Кілометри -> Милі\n 2. Метри -> Ярди\n 3. Метри -> Фути\n 4. Сантиметри -> Дюйми\
# \n 5. Миліметри -> Дюйми \n 6. Милі <- Кілометри \n 7. Ярди <- Метри \n 8. Фути <- Метри\
# \n 9. Дюйми <- Сантиметри\n 10. Дюйми <- Міліметри\n '))
# if dlina == 1:
# value_dlina = float(input('Скільки кілометрів? :\n'))
# print(value_dlina, 'кілометрів становить',
# round((value_dlina * 1.60934), 2), 'миль')
# elif dlina == 2:
# value_dlina = float(input('Скільки метрів? :\n'))
# print(value_dlina, 'метров становить', round(
# (value_dlina * 1.09361), 2), 'ярдів')
# elif dlina == 3:
# value_dlina = float(input('Скільки метрів? :\n'))
# print(value_dlina, 'метров становить', round(
# (value_dlina / 0.3048), 2), 'футів')
# elif dlina == 4:
# value_dlina = float(input('Скільки сантиметрів? :\n'))
# print(value_dlina, 'сантиметрів становить', round(
# (value_dlina * 2.5400013716), 2), 'дюймів')
# elif dlina == 5:
# value_dlina = float(input('Скільки міліметрів? :\n'))
# print(value_dlina, 'міліметрів становить', round(
# (value_dlina / 0.0393701), 2), 'дюймів')
# elif dlina == 6:
# value_dlina = float(input('Скільки миль? :\n'))
# print(value_dlina, 'миль =', round(
# (value_dlina / 0.621371), 2), 'кілометрів')
# elif dlina == 7:
# print(value_dlina, 'ярдів =', round(
# (value_dlina / 0.9144), 2), 'метрів')
# elif dlina == 8:
# value_dlina = float(input('Скількі футів? :\n'))
# print(value_dlina, 'футів =', round(
# (value_dlina / 3.28084), 2), 'метрів')
# elif dlina == 9:
# value_dlina = float(input('Скількі дюймів? :\n'))
# print(value_dlina, 'дюймів =', round((value_dlina / 0.393701), 2), 'сантиметрів')
# elif dlina == 10:
#  value_dlina = float(input('Скільки міліметрів? :\n'))
# print(value_dlina,'міліметрів становить', round((value_dlina / 0.0393701), 2) ,'дюймів')

############### END DZ ################
#
#
############### if else loops  ################

# a = int(("Enter first digit: "))
# b = int(("Enter second digit: "))
# if a > b:
# print("a > b")
# elif a < b:
# print("a < b")
# else:
# print("a = b")


# def sey_Hey():
# name = input("enter your name: ")
# print("Hello,", name)

# sey_Hey()

# def plus(a, b):
# return a + b

# sum = plus(3, 4)
# print(sum)
# def palus(*par)


#показуе коли температура була більша за 10 ща 7 днів##
# day = 0
# counter = 0
# while True:
# if day == 7:
#   break
# temp = int(input("Enter temper  "))
# day += 1
#  if temp > 10:
#       counter += 1
# print("Temp more 10", counter, "time.")

##########


# a = 10
# b = 10
# if a > b:
#   print("a > b")
# elif a < b:
#   print("a < b")
# else:
#   print("a = b")

# name =int (input("WWWWW00"))
# print("hi", name)
# print("type", type(name))


# a = int(input("type: "))
# b = int(input("type2: "))
# func = input("func: + - * /")
# if func == "+":
#   print(a + b)
# elif func == "/":
#   if b == 0:
#      print("Div 0")
# else:
#    print(a / b)
# elif func == "-":
#   print(a - b)
# elif func == "*":
#   print(a * b)

# Показуэ пору року

# a = int(input("tupe numb: "))
# if a == 1 or a == 2 or a == 12:
# print("winter")
# elif a == 3 or a == 4 or a == 5:
# print("весна")
# elif a == 6 or a == 7 or a == 8:
#  print("ЛІТО")
# elif a == 9 or a == 10 or a == 11:
#  print("Осынь")
# else :
#  print("errror")

############### DZ ################
#####табличка множення на введене число###

# a = int(input("tupe numb: "))
# for i in range(a, 10):
# for j in range(1, 10):
# print ('{} x {} = {}'.format(i, j, i*j), end=' ')
# print()

##########

# from random import randint

# trying = 1

# while True:

# rand = randint(1, 6)
# print(rand)
# if rand != 6:
# trying += 1
# else:
# break
# print("Try number ", trying)
# input("Your turn ===>", trying)


# import random

# def rollDie():
# return random.choice([1,2,3,4,5,6])

# def winFraction(): # Perform one trial of 10000 games and return fraction of wins for A
# winsA = 0 # only count wins for A
# for numTrow in range(6):
# isPlayerA = True # Player A always takes the first turn
# throw = rollDie()
# while throw != 6: # While the game is not over yet:
# isPlayerA = not isPlayerA # Switch to the other player
# throw = rollDie()
# if isPlayerA:
# winsA += 1 # Only count the wins for player A
# return winsA # This is the fraction: we know the number of played games

# def sim():
# for trial in range(2): # Perform 10 trials
# print(winFraction()) # Print the result of the trial

# sim() # Start the simulation

# from random import randint
# print("\nАзартні ігри шкідливі для вашого здоровя")
# dice_player = 0
# pc_dice = 0
# count = 0
# while True:
#     count += 1
#     input("\nНатисніть Enter для Гри")
#     dice1 = randint(1, 6)
#     dice2 = randint(1, 6)
#     if dice1 == dice2:
#         dice_player += 1
#         print("Good work")
#     result = dice1 + dice2
#     print("Спроба User","Кубик 1:" ,dice1, "та Кубик 2:", dice2)
#     dice_pc1 = randint(1, 6)
#     dice_pc2 = randint(1, 6)
#     if dice_pc1 == dice_pc2:
#         pc_dice +=1
#         print("Good Work SKYNET")
#     result_skynet = dice_pc1 + dice_pc2
#     print("Спроба SKYNET","Кубик 1:",dice_pc1, "та Кубик 2:", dice_pc2)

#     if result > result_skynet:
#         dice_player += 1
#     elif result < result_skynet:
#         pc_dice += 1
#     if dice_player == 6 or pc_dice == 6:
#         break
#     print ("Ваш результат: ", dice_player,"\nРезультат SKYNET: ", pc_dice)
# if pc_dice < dice_player:
#     print("Виграв User з кількістю балів: ", dice_player )
# else:
#     print("Виграв SKYNET ", pc_dice,"балів")

# arf = [1, 42, 16, 18]
# print(arf)
# arf.append(28)  # добавити в масив
# print(arf)
# ставимо в масив 1) цифра на яке місце ставимо 2) число яке вставояємо
# arf.insert(2, 100500)
# print(arf)
# arf.remove(100500)
# print(arf)  # видаляє перше (100500)
# arf.clear()  # чистить повныстю масив
# print(arf)
# arf.append(599)  # добавити в масив
# print(arf)
# arf.append(185)  # добавити в масив
# print(arf)
# arf.append(25)  # добавити в масив
# print(arf)
# arf.append(385)  # добавити в масив
# print(arf)

# print(arf.index(25)) # вертає номер індекса


# arf.pop(1) # видаляэ номер індекса з масива
# print(arf)
# arf.count(8)
# print(arf)
# print(arf)
# arf.append("microsoft")
# print(arf)
# arf.sort()
# print(arf)
# arf.reverse()
# print(arf)

# print(len(arf))
# print(min(arf))
# print(max(arf))

# for ihem in (arf):
#    print(arf)
# import copy
# name = ["Bill", "Dian", "Tomm", "Stop", "Dice", "Form"]
# name.sort()
# for ithem in (name):
#     print(name)

# name1 = ["Tom", "Vim", "Bill", "Vork"]
# #name2 = name1
# name2 = copy.deepcopy(name1)
# print("name1", name1)
# print("name2", name2)
# name2.append("Brend")
# print("name1", name1)
# print("name2", name2)
# name3 = name1[3:5]
# print(name3)


###############
# Дано одновимірний масив. Знайти найбільший та найменший елементи масиву та поміняти їх у масиві місцями.
##################
# mass = [1, 2, 5, 56, 7, 87, 98, 0, 34, 123, 545, 6, 7, 8888]
# print(mass)
# min_value = min(mass)
# max_value = max(mass)
# min_index = mass.index(min_value)
# max_index = mass.index(max_value)
# temp=mass[min_index]
# mass[min_index] = mass[max_index]
# mass[max_index] = temp
# print("New Arr", mass)


################################
# Дано одновимірний масив. Знайти суму елементів з непарними індексами.
##################################
# N = [1, 2, 5, 56, 7, 87, 98, 0, 34, 123, 545, 6, 7, 8888]
# s = sum(N[1: :2])
# print(s)

# N = [1, 2, 5, 56, 7, 87, 98, 0, 34, 123, 545, 6, 7, 8888]
# N2 = [1, 2, 5, 56, 7, 87, 98, 0, 34, 123, 545, 6, 7, 55]
# s = sum()

# http://www.cyberforum.ru/python-beginners/thread1737276.html

##########################################
# Дано список. Знайти найбільший та найменший елементи
# масиву та поміняти їх у масиві місцями.
# from random import random
# N = 15
# arr = [0]*N
# for i in range(N):
#     arr[i] = int(random()*10)
#     print(arr[i],end='')
# print()
# mn = min(arr)
# mx = max(arr)
# imn = arr.index(mn)
# imx = arr.index(mx)
# print('arrmin[%d]=%d arrmax[%d]=%d' % (imn+1, mn, imx+1, mx))
# arr[imn], arr[imx] = arr[imx],arr[imn]
# for i in range(15):
#     print(arr[i],end='')
# print()
#
#############################################
# Дано список. Поміняти місцями перший елемент з другим, третій з четвертим,
# і т.д. Вивести змінений масив на екран
# arr = list(map(int,input('Введіть деяку кількість чисел через пробіл: ').split()))
# print(arr)
# k = 1
# for i in range(len(arr)//1):
#     print("\nБуло - ", i, arr)
#     arr[k], arr[i] = arr[i], arr[k]
#     print("стало - ", arr)
#     k = -1

# розділяє список на дві частини від заданого інтервалу
# A = [0, 1, 2, 3, 4, 5]
# B = A[:3]
# C = A[3:]
# print(B,C)
# a = int(input("Введіть початок інтервалу: "))
# b = int(input("Введіть кінець інтервалу: "))
# spisok = [1,2,3,4,5,6,7,8,9,10,22,33,44,55,11,34]
# interval = range(a, b + 1)
# ps1 = []
# ps2 = []
# for x in spisok:
#     if x in interval:
#         ps1.append(x)
#     else:
#         ps2.append(x)
# print("Список K: ", spisok)
# print("Список B --> ", ps1)
# print("Список C -->",ps2)


# class Person:
#     name = "Bill"
#     def showe_person(self):
#         print("Hello", self.name)
# Bill = Person()
# Bill.showe_person()
# Tom = Person()
# # Tom.showe_person()
# Tom.name = "Tom"
# Tom.showe_person()


# class Person:
#     def __init__(self, name):
#         self.__name = name
#         print("Person constructor", self.__name)

#     def __del__(self):
#         print("PersonDestructot", self.__name)

#     def __showe_person(self):
#         print(self.__name)


# Jack = Person("Jack")
# Jack.showe_person()
# Bobic = Person("Bobic")
# Bobic.showe_person()

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     def set_name(self, new_name):
#         if self.__name == new_name:
#             print("theseve name")
#         else:
#             self.__name == new_name


# Bill = Person("Bill")
# print(Bill.set_name())
# from random import randint

# class Account:
#     def __init__(self, card_number, amount, currancy):
#         self.__card_number = card_number
#         self.__amount = amount
#         self.__currancy = currancy
#         self.__new_amount = 0

#         print("FFFFFFF")
#     def show_info(self):
#         print("Card namb: ", self.__card_number, "\nAmount: ", self.__amount, "\nCurrancy: ", self.__currancy)
#     def increment_amount(self, amount):
#         self.__new_amount += int(input("Text: "))


# amount = int(input("Enter money: "))
# currancy = input("Enter carrncy: UAN USD EUR \n--->")
# card_number = randint(10000, 99999)

# credit_card = Account(card_number, amount, currancy)
# credit_card.show_info()

# credit_card.increment_amount(0)
# credit_card.show_info()
 #----------------------------------------------------------------------------------------------------------------------------------------------
# class Person:
#     def __init__(self, name:str, surname:str, age: int):
#         self.__name:str = name
#         self.__surname:str = surname
#         self.__age:int = age

#     def show_person(self):
#         print("Name: ", self.__name, "\nsurname: ", self.__surname, "\nAge: ", self.__age)

#     @property
#     def name(self):
#         return  self.__name 
#     @name.setter
#     def name(self, new_name:str):
#         self.__name = new_name

#     @property
#     def surname(self):
#         return self.__surname
#     @surname.setter
#     def surname(self, new_surname:str):
#         self.__surname = new_surname    

#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, new_age:int):
#         self.__age = new_age    

# class Junior (Person):
#     def __init__(self, name:str, surname:str, age:int, skills:str, position:str):
#         Person.__init__(self, name, surname, age)
#         self.__skills = skills
#         self.__position = position
#     def show_person(self):
#         print("Name: ", self.name, "\nsurname: ", self.surname, "\nAge: ", self.age, "\nskills :", self.__skills, "\nposition :", self.__position) 

# jun = Junior("Patrik", "Tresher", 36 , "Top_Junior", "Full Gobe")
# jun.show_person()
# print("-----------------------------------")
# jun.name = "Tripe"
# jun.surname = "Prymus"
# jun.age =24
# jun.show_person()
# gvido = Person("Gvido", "Van", 46)
# gvido.show_person()
# print("____--------______")
# print("prop before -->", gvido.name)
# gvido.name = "Tupak"
# gvido.surname = "DuVan"
# gvido.age = 55
# gvido.show_person()
# print("prop after -->", gvido.name)                    
        

        