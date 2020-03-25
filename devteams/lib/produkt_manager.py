from lib.employees import Employees

if __name__ == "__main__":
    add_pmanadger()


class Pmanager(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills = skills


def add_pmanadger():
    try:
        name = str(input("Введіть імя Produkt менеджера ===> "))
        surname = str(input("Введіть фамілію Produkt менеджера ===> "))
        age = int(input("Введіть вік Produkt менеджера ===> "))
        salary = int(input("Введіть зарплату Produkt менеджера ===> "))
        skill = str(input("Напишіть навички(скілзи) Produkt менеджера ===> "))
        new_pmanadger = Pmanager(name, surname, age, salary, skill)
        return new_pmanadger
    except:
        print("ERROR. Невірно введені дані(цифри-літери)")
