def print_table(num, operation):
    results = []
    for i in range(1, 11):
        if operation == '+':
            result = num + i
        elif operation == '*':
            result = num * i
        results.append(result)

    for i, res in enumerate(results, start=1):
        print(f'{num} {operation} {i} = {res}')
    print(f'sum is {sum(range(num, num + 10))}')

def get_sum(num, operation):
    results = []
    for i in range(10):
        if operation == '+':
            result = num + i
        elif operation == '*':
            result = num * i
        results.append(result)
    return results

if __name__ == '__main__':
    try:
        num = int(input("Enter the number: "))
        operation = input("Enter the operation (+ or *): ")
        results = get_sum(num, operation)
        print_table(num, operation)
    finally:
        print('Program is finished')