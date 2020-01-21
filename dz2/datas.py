print("Дати\n7.1\n8.4\n12.9\n1.4\n10.5\n14.10")
data = int(input("Введіть день : "))
mis = int(input("Введіть місяць: "))

def holiday(mis, data):
    if mis == 1 and data == 7:
        print("\n  ✿´*•7.01•*´✿\nРіздво Христове")
    elif mis == 4 and data == 8:
        print("\n  ✿´*• 8.04 •*´✿\nМіжнародний Жіночий день")
    elif mis == 9 and data == 12:
        print("\n 10010№?# 12.09 №?#0101\nМіжнародний День Програміста")
    elif mis == 4 and data == 1:
        print("\n  o_O 1.04 :P :D\nДень Сміху")
    elif mis == 5 and data == 10:
        print("\n   ✿´*´*✿•10.05•✿*´✿ \nДень Матері")
    elif mis == 10 and data == 14:
        print("\n   14.10 \nДень українського козацтва\nДень захисника України")
    else:
        print("ПЕРЕПРОШУЄМО ТАКИХ ДАТ МИ ЩЕ НЕ ДОБАВИЛИ....")
holiday(mis, data)