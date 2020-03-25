from lib.developer import Developer, add_developer
from lib.hr_manager import HRmanager, add_hrmanager 
from lib.business_analyst import BAnalyst, add_banalyst
from lib.tester import Tester, add_tester
from lib.produkt_manager import Pmanager, add_pmanadger
from lib.employees import Employees


import pickle


all_employees = []


def my_file(all_employees):
    my_file = open("emploees.txt", "w")
    my_file.write(str(all_employees))
    my_file.close()
       

def show_info_employees():
    print("Employees")
    i = 1
    for item in all_employees:
        print(f" Id:{i}  \n Name: {item.name} \n Surname: {item.surname} \n Age: {item.age} \n Salary: {item.salary} \n Skills: {item.skills}")
        i += 1

exit = False
while not exit:
    print("--- Команда Спеціалістів ---")
    print("""
    1. Показати список робітників
    2. Додати робітника
    3. Bидалити робітника
    4. Зберегти у файл
    0. Вихід
    """)
    try:
        choice = int(input())
        if choice == 1:
            show_info_employees()
        elif choice == 2:
            print("Виберівть працівника якого хочете добавити")
            print("""
            1. Девелопер
            2. Тестер
            3. Бізнес- аналітик
            4. HR менеджер
            5. Продакт-менеджер
            """)
            work = int (input())
            if work == 1:
                position = add_developer()
                all_employees.append(position)
                # add_employees(add_developer)
            elif work == 2:
                position = add_tester()
                all_employees.append(position)
                # add_employees(add_tester)
            elif work == 3:
                position = add_banalyst()
                all_employees.append(position)
                # add_employees(add_banalyst)
            elif work == 4:
                position = add_hrmanager()
                all_employees.append(position)
                # add_employees(add_hrmanager)
            elif work == 5:
                position = add_pmanadger()
                all_employees.append(position)
                # add_employees(add_pmanadger)
            elif work == 0:
                break
        elif choice == 3:
            show_info_employees()
            choise_del = int(input("Введіть номер для видалення"))
            all_employees.pop(choise_del-1)
            show_info_employees()
        elif choice == 4:
            my_file(all_employees)
        elif choice == 0:
            exit = True 
        else:
            print("Читайте правила")  
    except Exception as error:
        print("Error ===> ", error)  

    
    
      





