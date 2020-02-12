import colorama
from colorama import Fore, Back, Style
colorama.init()

if __name__ == "__main__":
    phone_add()
    phone_delete()
    phone_sort()
    phone_sell()
    phone_sell_stata()
    items_phon()


def phone_add(phone):
    new_phone_name = input("Введіть назву телефона: ")
    new_phone_model = input(
        "Введіть модель телефона(латиницею на приклад'11 pro Max 128Gb'): ")
    try:
        new_phone_cost = int(input("Введіть ціну телефона(в гривнях): "))

        phone.append({"id": len(phone)+1, "name": new_phone_name,
                      "model": new_phone_model, "price": new_phone_cost})
    except:
        print(Fore.YELLOW + Back.BLUE +
              "\nError Ціна введена була не вірно, потрібно ввести цифри")
        print(Style.RESET_ALL)


def phone_delete(phone):
    del_phones = input("Введіть номер телефона зі списку для його видалення: ")
    phone.pop(int(del_phones)-1)
    input("Натисни Enter для продовження")


def phone_sort(phone):
    phones_sort = int(
        input("Сортувати по: \nid : 1\nprice : 2\nname : 3\n\t -->"))
    if phones_sort == 1:
        phones_sort = "id"
    elif phones_sort == 2:
        phones_sort = "price"
    else:
        phones_sort = "name"

    sort_ph = sorted(phone, key=lambda phone: phone[phones_sort])

    input("Натисни Enter для перегляду результата")
    return sort_ph


def phone_sell(phone):
    for item in phone:
        print(item['id'], ("="), item["name"], ('|'),
              item['model'], ('|'), str(item['price']))
    sell = input(
        "Введіть номер телефона зі списку, який ви хочете придбати: \n---> ")
    for item in phone:
        return phone.pop(int(sell)-1)


def phone_sell_stata(soled):
    print("[", soled, "]--> Телефонів було продано\n")
    input("Натисни Enter для продовження")


def items_phon(phone):
    for item in phone:
        print(item['id'], item["name"], ('|'),
              item['model'], ('|'), str(item['price']).join('[]'))
