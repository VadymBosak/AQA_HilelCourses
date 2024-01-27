# 1 - Є 3 группи людей(sets) australia_blacklist, poker_blacklist, alcohol_blacklist. \
# В кожній групі вказані імена. Вивести тих хто виграв джекпот(є одразу в 3х списках)

australia_blacklist = {'John', 'Max', 'Alex'}
poker_blacklist = {'Hanna', 'Alex', 'Andrew'}
alcohol_blacklist = {'Joe', 'Alex', 'Den'}

jackpot_winner = australia_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(jackpot_winner)
print('\n')

# 2 - Словник має наступні дані: {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}
# Використвоючі f-string вивести: "User_name is living in place_name" для кожного юзера. Використовувати цикл

user_names = {'Alex': 'house', 'Max': 'Flat', 'Olha': 'Appartments', 'Oleh': 'Trench'}

for name in user_names:
    print(f'{name} is living in {user_names[name]}')
print('\n')


# 3 - Є список ['Jack', 'Leon', 'Alice', None, 32, 'Bob']
# Вивести ТІЛЬКИ коректні імена(тобто стрінги). Використовувати Continue.

names_list = ['Jack', 'Leon', 'Alice', None, 32, 'Bob']

for name in names_list:
    if type(name) == str:
        print(name)
    continue
print('\n')


# 4 - Порахувати та вивести(print) кількість букв в строці.
#
# Юзер щось вводить(input)
# Ваша задача надрукувати кількість кожного символу того що він ввів.
#
# Прикдад:
# Юзер вводить:
# My name is Emmy Santiago.
#
# ВИ прінтаете щось накшталт:
# M = 1, y = 2, n = 2, ...(або в іншому форматі, це не принциповоб головне, що б чітко було зрозуміло скільки разів
# зустрічаеться кожна буква)
#
# Тобто кожну букву та скільки разів вона зустрічаеться
#
# Підказка: це про словники, get можна використати для того щоб витягнути чи є ключ без помилки
# та надати дефолтне значення

dict_input = input("Let's count each character amount: ")
dict_counter = {}

for character in dict_input:
    if character.isspace():
        continue
    dict_counter[character] = dict_counter.get(character, 0) + 1

for character, count in dict_counter.items():
    print(f"{character}: {count}")



# 5 Задача без оцінювання:
#
# Ви створюєте список в якому може бути None(а може і не бути)
# Мета: надрукувати "There is no None" у випадку якщо None не зустрічаеться у списку
#
# Умови:
# По списку ми йдемо циклом
# Не створювати змінні(крім списку про який сказано вище)
# використати if 1 раз
# Не використовувати методи/функції/класи

my_list = ['Alex', 'John', None, 'Bob']

for element in my_list:
    if element is None:
        break

else:
    print('There is no None')


# 6 Задача без оцінювання
# Вирішити задачу 4 без словника за 2 строки:
# 1 строка це input
# 2 строка це рішення

dict_input = input("Let's count each character amount: ")
print([(char, dict_input.count(char)) for char in set(dict_input) if char != ' '])