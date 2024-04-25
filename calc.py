import math
def summa (first, second):
    if (type(first) is not int) and (type(first) is not float):
        raise ValueError
    if (type(second) is not int) and (type(second) is not float):
        raise ValueError
    return first + second


def sub (first, second):
    if (type(first) is not int) and (type(first) is not float):
        raise ValueError
    if (type(second) is not int) and (type(second) is not float):
        raise ValueError
    return first - second


def mult (first, second):
    if (type(first) is not int) and (type(first) is not float):
        raise ValueError
    if (type(second) is not int) and (type(second) is not float):
        raise ValueError
    return first * second


def div (first, second):
    if (type(first) is not int) and (type(first) is not float):
        raise ValueError
    if (type(second) is not int) and (type(second) is not float):
        raise ValueError
    if second==0:
        raise ArithmeticError
    return first / second

def degree(first, second):
    if (type(first) is not int) and (type(first) is not float):
        raise ValueError
    if (type(second) is not int) and (type(second) is not float):
        raise ValueError
    return first ** second

def sqrt(first):
    if (type(first) is not int) and (type(first) is not float):
        raise ValueError
    if first<0: raise ArithmeticError
    return first ** (1 / 2)

def factorial(first):
    if type(first) is not int:
        raise ValueError
    if first < 0: raise ArithmeticError
    return math.factorial(first)

def calc(first, second, oper):

    result = None

    if oper == '+':

        result = summa(first, second)

    elif oper == '-':

        result = sub(first, second)

    elif oper == '*':

        result = mult(first, second)

    elif oper == '/':

        if (second == 0):

            print('Деление на ноль запрещено!')

            return

        result = div(first, second)

    elif oper == '!':
        result = factorial(first)

    elif oper == '**':

        result = degree(first, second)

    elif oper == 'sqrt':

        result = sqrt(first)

    else:

        print('Некорректная операция!')

    return result


def operation():

    mes = input('Выберите операцию (Введите +, -, *, /, %, **, log):\n '

                '+ - сложение двух чисел\n'

                '- - вычитание двух чисел\n'

                '* - умножение двух чисел\n'

                '/ - деление двух чисел\n'

                '! - факториал числа\n'

                '** - возведение первого числа в степень второго\n'

                'sqrt - извлечение квадратного корня''\n')

    if mes == '+':

        print('Вы выбрали сумму')

    elif mes == '-':

        print('Вы выбрали разность')

    elif mes == '*':

        print('Вы выбрали умножение')

    elif mes == '/':

        print('Вы выбрали деление')

    elif mes == '!':

        print('Вы выбрали факториал')

    elif mes == '**':

        print('Вы выбрали возведение в степень')

    elif mes == 'sqrt':

        print('Вы выбрали извлечение квадратного корня')


    correct_operations = ['+', '-', '*', '/', '!', '**', 'sqrt']

    while mes not in correct_operations:

        print('Такой операции нет в списке. Попробуйте ещё!')

        mes = input()


    return mes


def run():
    op = operation()
    second = 1
    try:

        first = float(input('Укажите первое число: '))

    except ValueError:

        first = float(input('Вы ввели некорректные данные. Пожалуйста, введите целое число.'))

    if (op != '!'):
        if(op != 'sqrt'):
            try:

                second = float(input('Укажите второе число: '))

            except ValueError:
                second = float(input('Вы ввели некорректные данные. Пожалуйста, введите целое число.'))

    result = calc(first, second, op)

    print(f'Результат: {result}')


