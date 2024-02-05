# 2) Створіть 2 функції

# get_sum та print_table(імена можете вказувати на ваш розсуд)
#
# 1) get_sum викликає print_table всередині себе

# 2) get_sum приймає 2 значення: число та операцію +,*(тобто get_sum(num: int, operation:str) )
# та повертає результат додавання числа та наступнийх 9ти після нього(тобто результат додавання 10 цифр)

# 3) print_table друкує таблицю з числом та операцєю які було передано в get_sum від 1 до 10
# вважайте, що юзер завжди вводить правильно операцію та число
#
# Приклад виклику:
# if __name__ == '__main__':
# print('sum is', get_sum(5, '*'))
#

def print_table(num, operation, result):
    for i, result in enumerate(result, start=1):
        print(f'{num} {operation} {i} = {result}')

def get_sum(num, operation):
    results = []
    for i in range(1, 11):
        if operation == '+':
            result = num + i
        elif operation == '*':
            result = num * i
        results.append(result)
    print_table(num, operation, results)
    return sum(results)

if __name__ == '__main__':
    try:
        num = int(input("Enter the number: "))
        operation = input("Enter the operation (+ or *): ")
        print('sum is', get_sum(num, operation))
    finally:
        print('Program is finished')