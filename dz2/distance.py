cars = input("Яка марка вашого автомобіля?: ")
distance = float(input("Введіть відстань яку ви хочете подолати (км): "))
palyne = float(input("Яку кількість пального споживає авто на 100(км):  "))

def result(distance, palyne):
    res = distance / 50 * palyne
    print("Ваш автомобіль " + cars + " витратить " +
         str(res) + " літрів палива в обидві сторони!")
    print("Щасливої дороги!")
result(distance, palyne)
