# coding=utf-8
import math, defs


num1 = float(input('1е число: '))
oper = input('Действие: ')
num2 = float(input('2е число: '))
result = None


sub = defs.minus
mul = defs.mul
add = defs.add
del_slash = defs.del_slash
factorial = defs.factorial


calculator = {
    '*': mul,
    '-': sub,
    '+': add,
    '/': del_slash,
    '**': factorial
}


try:
    if oper in list (calculator.keys()):
        result = calculator[oper](num1, num2)
    else:
        raise Exception('Вы не ввели действие которое нужно выполнить с числами!! Например: ( +, -, *, /, ** )')
except Exception as e:
    print(e)


if result is not None:
    print(result)