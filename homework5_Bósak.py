# 1
# Дано список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
#
# Лише за допомогою функцій map, lambda, zip(необов'зково) створити та надрукувати словник квадратів цих чисел
#
# Очікуваний результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

result = list(map(lambda x: int(x) ** 2, str_list))
print(result)
print('\n')

# 2
# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора
# (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).
#
# Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
# Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
# Якщо введені числа не можуть бути float спіймайте ValueError
#
# Також ловіть помилку при діленні на 0
#
# В кожній спійманій помилці друкуйте пояснення, що пішло не так
# Надайте три спроби скористуватись калькулятором, якщо введені не вірні дані,
# якщо не вийшло - прінтайте що закінчились спроби
#
# Результат виконання формули - float число з двома знаками після крапки

class FormulaError(Exception):
    pass

class WrongOperatorError(Exception):
    pass

calculation = lambda x, operator, y: {
    '*': x * y,
    '/': x / y if y != 0 else "Division by 0",
}.get(operator, "Unsupported operator")

max_attempts = 3
attempts_left = max_attempts

while attempts_left > 0:
    user_input = input(f'Enter the formula, like 2 * 5: ')

    try:
        params = user_input.split()

        if len(params) != 3:
            raise FormulaError('Entered data should contain 3 elements')

        number1 = float(params[0])
        operator = params[1]
        number2 = float(params[2])

        if operator not in {'*', '/'}:
            raise WrongOperatorError("Second element should be '*' or '/'")

        if number2 == 0:
            raise ZeroDivisionError('Division by 0 is not allowed')

        result = calculation(number1, operator, number2)

        formatted_result = "{:.2f}".format(result)

        result = round(result, 2)

        print(f'Result: {formatted_result}')

        if formatted_result:
            break

    except ZeroDivisionError:
        print("Division by 0 is not allowed")
        attempts_left -= 1

    except ValueError:
        print("Enter a valid numeric values")
        attempts_left -= 1

    except FormulaError:
        print('Entered data should contain 3 elements')
        attempts_left -= 1

    except WrongOperatorError:
        print('Second element is not «*» or «/»')
        attempts_left -= 1

    if attempts_left == 0:
        print("The attempts are over.")