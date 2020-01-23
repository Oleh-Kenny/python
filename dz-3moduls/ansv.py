from mod.modul import *
counter = 0
print("Розпочинаємо тест")

if g1() == "2":
    counter += 1
if g2() == "1":
    counter += 1
if g3() == "2":
    counter += 1
if g4() == "1":
    counter += 1
if g5() == "3":
    counter += 1
if g6() == "4":
    counter += 1
if g7() == "1":
    counter += 1
if g8() == "3":
    counter += 1
if g9() == "2":
    counter += 1
if g10() == "4":
    counter += 1
if g11() == "3":
    counter += 1
if g12() == "2":
    counter += 1

print("Ваш результат", counter)

if  counter >= 10:
    print("Відмінно, молодець, так продовжувати")
elif  counter >= 7:
    print("Добре, молодець, але потрібно ще попрацювати")
elif counter  >= 4:
    print("Слабенько, але ти молодець, працюй більше")
else:
    print("Погано, потрібно быльше працювати")
