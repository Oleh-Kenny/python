def g1():
    answ = input(
        "What is the output of for x in [1,2,3]:print x?: \n\t1 x x x \n\t2 1 2 3 \n\t3 Нічого з цього\n\t"
    )
    return answ
# 2)


def g2():
    answ = input(
        "What is the output of L[1:] if L=[1,2,3]?: \n\t1 2,3 \n\t2 2 \n\t3 3 \n\t4 Друга відповідь...\n\t"
    )
    return answ
# 1)


def g3():
    answ = input(
        "[(a,b)for a in range(3) for b in range(a)]?: \n\t1 [(1,0),(2,1),(3,2)] \n\t2 [(0,0),(1,1),(2,2) \n\t3 [(1,0),(2,1),(2,1)] \n\t4 [(1,0),(2,0),(2,1)]]\n\t"
    )
    return answ
# 2)


def g4():
    answ = input(
        "," ".join(['1','2','4','8','16']) : \n\t1 '1, 2, 4, 8, 16' \n\t2 '1,2,4,5,16' \n\t3 (1,2,4,8,16) \n\t4 [1,2,4,8,16]\n\t"
    )
    return answ
# 1)


def g5():
    answ = input(
        "Какая из функцый вернет итерирукмый объект?: \n\t1 len() \n\t2 xrange() \n\t3 range() \n\t4 ord()\n\t"
    )
    return answ
# 3)


def g6():
    answ = input(
        "Что такое инкапсуляция?: \n\t1 Специальная функция, означающая какие функции выполнить нельзя \n\t2 разбивка программы на отдельные файлы с классами \n\t3 специальний класс, который используется для тестирования \n\t4 инкапсуляция делает некорорые из компонентов доступными внутри класса\n\t"
    )
    return answ
# 4)


def g7():
    answ = input(
        "Где будет быстрее поиск? при условии 1млн записей. : \n\t1 dict \n\t2 list \n\t3 set \n\t4 tuple\n\t"
    )
    return answ
# 1)


def g8():
    answ = input(
        "Что выведет следующий код, при его исполнении? Используется Python 3.x. print(type(1/2)) \n\t1 class'int' \n\t2 class'number' \n\t3 class'double' \n\t4 class'tuple'\n\t"
    )
    return answ
# 3)


def g9():
    answ = input(
        " def a(b,c,d):pass - ?: \n\t1 Определяет список и инициализирует его. \n\t2 Определяет функцию, которая ничего не делает. \n\t3 Определяет функция, которая передает параметры. \n\t4 Определяет пустой класс\n\t "
    )
    return answ
# 2)


def g10():
    answ = input(
        "Где правильно создана переменная? : \n\t1 int num = 2 \n\t2 $num = 2 \n\t3 var num = 2 \n\t4 num = float(2) \n\t5 Нет подходящего варианта\n\t"
    )
    return answ
# 4)


def g11():
    answ = input(
        "Какое значение получит а? a =2,3 : \n\t1 2 \n\t2 3 \n\t3 (2,3)\n\t "
    )
    return answ
# 3)


def g12():
    answ = input(
        "Что напечатает следующий код - print*((1,2,3)<(1,2,4)) \n\t1 None \n\t2 True \n\t3 False \n\t4 Ошибка\n\t"
    )
    return answ

# 2)
if __name__ == "__main__":
    g1()
    g2()
    g3()
    g4()
    g5()
    g6()
    g7()
    g8()
    g9()
    g10()
    g11()
    g12()
