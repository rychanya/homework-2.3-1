def user_input():
    print('')
    try:
        operator, number_one, number_two = input().split(' ')
    except ValueError:
        print('Некоректное количество аргументов. Попробуйте еще раз.')
        return user_input()
    try:
        number_one = int(number_one)
        number_two = int(number_two)
    except ValueError:
        print('введены не числа. Попробуйте еще раз.')
        return user_input()
    return (operator, number_one, number_two)


def calculate(operator, number_one, number_two):
    assert operator in {'+', '-', '*', '/'}, 'Недопустимый оператор.'
    if operator == '+':
        return number_one + number_two
    elif operator == '-':
        return number_one - number_two
    elif operator == '*':
        return number_one * number_two
    elif operator == '/':
        try:
            return number_one / number_two
        except ZeroDivisionError:
            print('Деление на ноль')


if __name__ == '__main__':
    operator, number_one, number_two = user_input()
    print(f'Результат {calculate(operator, number_one, number_two)}')
       