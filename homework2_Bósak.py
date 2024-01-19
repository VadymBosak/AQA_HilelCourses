# task 1
celsius_t = int(input('Enter the temperature in Celsius: '))

fahrenheit_t = celsius_t * 9/5 + 32.0
kelvin_t = celsius_t + 273.15

print(fahrenheit_t)
print(kelvin_t)
print('***')

#task 2

number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
operation = input('Enter the arithmetic operation (+, -, *, /): ')

if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    if number2 == 0:
        print('The second number cant be 0 for "/" operation')
    else:
        print(number1 / number2)
else:
    print('Unknown operator')