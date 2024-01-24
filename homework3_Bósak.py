# Задача
#
# Створити динамічний список покупок.
#
# Юзер має можливість додати продукти до списку
#
# Юзер має можливість видалили продукти зі списку
#
# Про зміні списку новий список друкуеться
#
# Якщо список порожній про це пишеться і програма закінчує роботу
#
# Алгоритм:
#
# 1) Запропонувати юзеру створити список(введіть продукти через пробіл)
#
# 2) Строку яку ввів юзер перевести в список
#
# 3) Надрукувати список який ввів юзер
#
# 4) Якщо юзер нічогоне ввів(або ввів лише пробіли) то написати список продуктів порожній і закінчити програму
#
# 5) Запропонувати юзеру ввести продукт та ознаку чи варто його видаляти чи додавати(якщо видаляти, то продукт
# починаеться з -
#
# 6) Додати/видалити продукт
#
# 7) Надрукувати оновлений список продуктів
#
# 8) Продовжувати поки список не стане порожнім
#
# Зверніть увагу:
#
# При виконанні завдання необідно використати: len, while, (pop, index або remove), split , if..else, in.
# Якщо чогось не буде це -1 бал за кожний невикористаний інструмент
#
# Бажано використати: startswith, slice(синтаксис [::]), f-strings, strip
#
# Задання не важке для реалізації(відносно), але треба все зібрати в купу і прям подумати як це все повинно працювати.

import sys

products_list = input('Enter the products list: ')

if not products_list or products_list.isspace():
    print('Products list is empty')
    sys.exit(1)

else:
    if products_list.isdigit():
        print("The products can't be numbers")
        sys.exit(1)

    else:
        products_list = products_list.split()
        print(products_list)
        # print(type(products_list))


while len(products_list) != 0:
    products_upd = input('Add or delete(-) the product: ')

    if products_upd.startswith('-') and products_upd[1:] in products_list:
        products_list.remove(products_upd[1:])
        print('Product removed. Updated list: ', products_list)

    else:
        products_list.append(products_upd)
        # products_list.extend(products_upd):
        # products_upd = products_upd.split()
        print('Product added. Updated list: ', products_list)

    # if products_list.extend(products_upd):
    #     products_upd = products_upd.split()
    #     print(products_list)

    # elif products_upd.startswith('-') and products_upd[1:] in products_list:
    #     products_list.remove(products_upd[1:])
    #     print(products_list)

    if not products_upd or products_upd.isspace():
        print("Products names can't be the whitespace or empty")

    elif products_upd.isdigit():
        print("The products can't be numbers")

    # if products_upd.startswith('-') and products_upd[1:] in products_list:
    #     products_list.remove(products_upd[1:])
    #     print(products_list)

# elif products_list.extend(products_upd):
#     products_upd = products_upd.split()
#     print(products_list)

# else:
# print(input('Add or delete(-) the products: '))

print("List is empty. Program finished.")