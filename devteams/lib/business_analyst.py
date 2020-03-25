from lib.employees import Employees

if __name__ == "__main__":
    add_banalyst()


class BAnalyst(Employees):
    def __init__(self, name: str, surname: str, age: int, salary: int, skills: str):
        Employees.__init__(self, name, surname, age, salary, skills)
        self.__skills = skills
  
   
def add_banalyst():
    try:
        name = str(input("Введіть і*мя бізнес аналітика --> "))
        surname = str(input("Введіть фамілію бізнес аналітика --> "))
        age = int(input("Введіть вік бізнес аналітика --> "))
        salary = int(input("Введіть заробтню плату бізнес аналітика --> "))
        skill = str(input("Напишіть навички бізнес аналітика --> "))
        new_banalyst = BAnalyst(name, surname, age, salary, skill)
        return new_banalyst
    except:
        print("Error. Неввірно введени тип даних(замість цифр-букви, букви замість цифр)")