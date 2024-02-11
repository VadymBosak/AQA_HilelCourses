# 1-
# Створіть декоратор, який виводить в консоль назву викликаної функції.
#
# Наприклад, створіть пару функцій для арифметичних операцій підсумовування та множення.
#
# Під час виклику цих функцій має бути повернутий результат операції, а ім’я викликаної функції
# має відображатися на консолі разом із результатом.
#
# Використовуйте __name__


def function_name(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print(f"Function: {function.__name__}")
        return result
    return wrapper

@function_name
def sum(x, y):
    return x + y

@function_name
def multiply(x, y):
    return x * y

print(sum(2, 2))
print(multiply(3, 3))


# 2-
#
# Створіть функцію, яка може друкувати квадрати парних чисел у діапазоні від 0 до 1000000000 включно.
# Рішення має працювати і не фрізити комп’ютер.

def print_squares(start, end):
    for num in range(start, end +1):
        if num %2 == 0:
            print(num ** 2)

print_squares(0, 1000000000)


# 3-
#
# Створіть декоратор, який повертає результат функції. а також час за який вона виконана.
# Підсказка (для фіксації часу імпортуйте модуль time: import time)

import time

def check_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result
    return wrapper

@check_time
def test_function(n):
   time.sleep(n)
   return f'Execution time {n} sec'

print(test_function(2))