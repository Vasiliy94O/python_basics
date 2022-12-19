"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""
#Task_4
def exp_func(x, y):
    try:
        if y < 0:
            exp_x = 1
            for i in range(y, 0):
                exp_x *= x
                i += 1
            return 1 / exp_x
        else:
            return 'Необходимо вводить целое отрицательное число!'
    except TypeError:
        return 'Вы ввели не число!'
    except ZeroDivisionError:
        return 'Вы пытаетесь делить на 0.'
print(exp_func(int(input('Введите действительное положительное число x: ')),
               int(input('Введите целое отрицательное число y: '))))
