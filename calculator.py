def calculator(x, y, operator):
    if y == 0 and operator == '/':
        return 'Not Possible'
    
    dict_ops = {
        '+': x + y,
        '-': x - y,
        '/': x / y,
        '*': x * y
    }

    return dict_ops[operator]

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))
operator = input('Enter the operator: ')

result = calculator(x, y, operator)

print(result)