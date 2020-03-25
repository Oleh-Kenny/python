from lib.employees import Employees

if __name__ == "__main__":
    add_hrmanager()


class HRmanager(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills = skills
    
   
def add_hrmanager():
    try:
        name = str(input("Введіть імя HR менеджера -->> "))
        surname = str(input("Введіть фамілію HR менеджера -->> "))
        age = int(input("Введіть вік HR менеджера -->> "))
        salary = int(input("Введіть заробітню плау HR менеджера -->> "))
        skill = str(input("Напишіть вміння(скіли) HR менеджера -->> "))
        new_hrmanager = HRmanager(name, surname, age, salary, skill)
        return new_hrmanager
    except:
        print("Error. Невірно задані дані")