                                                                          ############### DZ ################      




# ==================================================== #
# пора дня від введеного часу

#a = int(input("Введіть час: "))
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


#dlina = int(input(' 1. Кілометри -> Милі\n 2. Метри -> Ярди\n 3. Метри -> Фути\n 4. Сантиметри -> Дюйми\
        #\n 5. Миліметри -> Дюйми \n 6. Милі <- Кілометри \n 7. Ярди <- Метри \n 8. Фути <- Метри\
       # \n 9. Дюйми <- Сантиметри\n 10. Дюйми <- Міліметри\n '))
#if dlina == 1:
    #value_dlina = float(input('Скільки кілометрів? :\n'))
   # print(value_dlina, 'кілометрів становить',
          #round((value_dlina * 1.60934), 2), 'миль')
#elif dlina == 2:
    #value_dlina = float(input('Скільки метрів? :\n'))
   # print(value_dlina, 'метров становить', round(
        #(value_dlina * 1.09361), 2), 'ярдів')
#elif dlina == 3:
    #value_dlina = float(input('Скільки метрів? :\n'))
   # print(value_dlina, 'метров становить', round(
       # (value_dlina / 0.3048), 2), 'футів')
#elif dlina == 4:
   # value_dlina = float(input('Скільки сантиметрів? :\n'))
    #print(value_dlina, 'сантиметрів становить', round(
       # (value_dlina * 2.5400013716), 2), 'дюймів')
#elif dlina == 5:
   # value_dlina = float(input('Скільки міліметрів? :\n'))
   # print(value_dlina, 'міліметрів становить', round(
        #(value_dlina / 0.0393701), 2), 'дюймів')
#elif dlina == 6:
       # value_dlina = float(input('Скільки миль? :\n'))
        #print(value_dlina, 'миль =', round(
           # (value_dlina / 0.621371), 2), 'кілометрів')
#elif dlina == 7:
       ##print(value_dlina, 'ярдів =', round(
            #(value_dlina / 0.9144), 2), 'метрів')
#elif dlina == 8:
        #value_dlina = float(input('Скількі футів? :\n'))
        #print(value_dlina, 'футів =', round(
           # (value_dlina / 3.28084), 2), 'метрів')
#elif dlina == 9:
       # value_dlina = float(input('Скількі дюймів? :\n'))
        #print(value_dlina, 'дюймів =', round((value_dlina / 0.393701), 2), 'сантиметрів')
#elif dlina == 10:
      #  value_dlina = float(input('Скільки міліметрів? :\n'))
        #print(value_dlina,'міліметрів становить', round((value_dlina / 0.0393701), 2) ,'дюймів')


                                                                    ############### END DZ ################   
                                                                    # 
                                                                    # 
                                                                     ############### if else loops  ################      

#a = int(("Enter first digit: "))
#b = int(("Enter second digit: "))
#if a > b:
    #print("a > b")
#elif a < b:
   # print("a < b")
#else:
    #print("a = b")  
      

#def sey_Hey():
    #name = input("enter your name: ")
   # print("Hello,", name)

#sey_Hey()

#def plus(a, b):
    #return a + b

#sum = plus(3, 4) 
#print(sum)   
#def palus(*par)


#показуе коли температура була більша за 10 ща 7 днів##
#day = 0
#counter = 0
#while True:
    #if day == 7:
     #   break
    #temp = int(input("Enter temper  ")) 
   # day += 1
  #  if temp > 10:
 #       counter += 1
#print("Temp more 10", counter, "time.")

##########
























#a = 10
#b = 10
# if a > b:
#   print("a > b")
# elif a < b:
#   print("a < b")
# else:
#   print("a = b")

#name =int (input("WWWWW00"))
#print("hi", name)
#print("type", type(name))


#a = int(input("type: "))
#b = int(input("type2: "))
#func = input("func: + - * /")
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

#a = int(input("tupe numb: "))
#for i in range(a, 10):
    #for j in range(1, 10):
        #print ('{} x {} = {}'.format(i, j, i*j), end=' ')
    #print()

##########

#from random import randint

#trying = 1

#while True:
    
    #rand = randint(1, 6)
    #print(rand)
    #if rand != 6:
        #trying += 1
    #else:
        #break
#print("Try number ", trying)
#input("Your turn ===>", trying)


#import random

#def rollDie():
    #return random.choice([1,2,3,4,5,6])

#def winFraction(): # Perform one trial of 10000 games and return fraction of wins for A
    #winsA = 0 # only count wins for A
    #for numTrow in range(6):
        #isPlayerA = True # Player A always takes the first turn
        #throw = rollDie()
       # while throw != 6: # While the game is not over yet:
           # isPlayerA = not isPlayerA # Switch to the other player
           # throw = rollDie()
        #if isPlayerA:
            #winsA += 1 # Only count the wins for player A
    #return winsA # This is the fraction: we know the number of played games

#def sim():
    #for trial in range(2): # Perform 10 trials
       # print(winFraction()) # Print the result of the trial

#sim() # Start the simulation

from random import randint
print("\nАзартні ігри шкідливі для вашого здоровя")
dice_player = 0
pc_dice = 0
count = 0
while True:
    count += 1
    input("\nНатисніть Enter для Гри")
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    if dice1 == dice2:
        dice_player += 1
        print("Good work")
    result = dice1 + dice2
    print("Спроба User","Кубик 1:" ,dice1, "та Кубик 2:", dice2)
    dice_pc1 = randint(1, 6)
    dice_pc2 = randint(1, 6)
    if dice_pc1 == dice_pc2:
        pc_dice +=1
        print("Good Work SKYNET")
    result_skynet = dice_pc1 + dice_pc2
    print("Спроба SKYNET","Кубик 1:",dice_pc1, "та Кубик 2:", dice_pc2)

    if result > result_skynet:
        dice_player += 1
    elif result < result_skynet:
        pc_dice += 1
    if dice_player == 6 or pc_dice == 6:
        break           
    print ("Ваш результат: ", dice_player,"\nРезультат SKYNET: ", pc_dice)
if pc_dice < dice_player:
    print("Виграв User з кількістю балів: ", dice_player )
else:
    print("Виграв SKYNET ", pc_dice,"балів")         


