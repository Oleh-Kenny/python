print('Василина Премудра грала зі Змієм Гориничем у шашки. Василина зївши 3 шашки, а Змій 5 шашок вирішили грати далі')
z = 5
v = 3
t = 3
sumz = []
sumz1 = [3]
while True:
    z += z
    v_v = v*t
    t += 2
    print('Вона поїдає', v_v, 'шт ')
    print('Він поїдає', z, 'шт')
    sumz.append(z)
    sumz1.append(v)
    next_turn = input(
        "\nНаступний крок - натиснути Enter \nНатиснути \"a\" щоб завершитигру поїданням Васелини\nЗупинити гру \"b\"\nНадавати Змію по шиї натиснути \"c\"\n\tРезультат:"
    )
    if next_turn == "a":
        print("Змій поїдає Васелину на: ", len(sumz),
              "кроці гри.\n", "Зївши : ", sum(sumz), "шашок")
        break
    elif next_turn == "b":
        print("Змій не зміг зїсти Васелину і гра завершилась на: ",
              len(sumz), "кроці", "Васелина зїла всього: ", sum(sumz1))
        break
    elif next_turn == "c":
        print("\nМудрий Лінус Торвальдс  наніс сильний удар по шиї Змію. \
                \nІ з того часу всі жили довго і щасливо і використовували Linux\n\n\t\tThe END")
        break