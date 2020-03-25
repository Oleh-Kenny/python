from lib.employees import Employees

if __name__ == "__main__":
    add_developer()


class Developer(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills: str = skills
 
def add_developer():
    try:
        name = str(input("Введіть імя Девелопера --> "))
        surname = str(input("Введіть Фамілію Девелопера --> "))
        age = int(input("Введіть вік Девелопера --> "))
        salary = int(input("Введіть заробітню платню Девелопера --> "))
        skills = str(input("Напишіть навички(скіли ) Девелопера --> "))
        new_developer = Developer(name, surname, salary, age, skills)
        return new_developer
    except:
        print("Error. Невірно введені дані(цифри-букви)")
