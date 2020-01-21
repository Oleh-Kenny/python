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
elif pc_dice == dice_player:
    print("Нічия шматок м'яса, зіграємо ще раз?", dice_player, "and", pc_dice )    
else:
    print("Виграв SKYNET ", pc_dice,"балів")