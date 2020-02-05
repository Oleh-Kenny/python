from phon_mod import phone_add, phone_delete, phone_sort, phone_sell, phone_sell_stata, items_phon

phone = [{"id": 1, 'name': "Sony", 'model': "Xperia 10 Dual", "price": 7999},
         {"id": 2, 'name': "Asus", 'model': "ROG Phone 8/128GB", "price": 18888},
         {"id": 3, 'name': "Nokia", 'model': "7.2 4/64GB", "price": 6999},
         {"id": 4, 'name': "Google Pixel", 'model': "4 XL 6/128GB", "price": 23387},
         {"id": 5, 'name': "Meizu", 'model': "Pro 7 Plus 6/128GB", "price": 10299},
         {"id": 6, 'name': "Samsung", 'model': "Galaxy Fold 12/512GB", "price": 56999}]
soled = []
while True:
    print("\t\t=<=<=<==<= Home Work for Phones =>=>=>=>=\n1: Добавити телефон:\n2: Видалити телефон:\n3: Сортувати по:\n4: Продаnb телефон:\n5: Подивитись статистику:\n6: Переглянути, що лишилося:\n0: Вихід")
    write = input()

    if write == "0":
        print("Заходьте ще!")
        break
    elif write == "1":
        phone_add(phone)
        items_phon(phone)
        input("Натисни Enter для продовження")
    elif write == "2":
        phone_delete(phone)
        items_phon(phone)
    elif write == "3":
        phone = phone_sort(phone)
        items_phon(phone)
    elif write == "4":
        soled.append(phone_sell(phone))
        items_phon(phone)
        print(soled)
    elif write == "5":
        phone_sell_stata(len(soled))
        items_phon(phone)
    elif write == "6":
        items_phon(phone)
