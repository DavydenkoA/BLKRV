'''
Подвиг 1. На вход программе подаются целые числа, записанные через пробел. Прочитайте эту строку и сохраните через
какую-либо переменную.

Напишите функцию, которая имеет один параметр, преобразовывает переданную ей строку в список чисел и возвращает
их сумму.

Определите декоратор для этой функции, который имеет один параметр start - начальное значение суммы.
Примените декоратор со значением start=5 к функции и вызовите декорированную функцию для прочитанной строки.
Результат (сумму) отобразите на экране.

Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.12.1

Sample Input:

5 6 3 6 -4 6 -1
Sample Output:

26
'''
def df_decor(start):
    def func_decor(func):
        def wrapper(s):
            res = func(s) + start
            return res
        return wrapper
    return func_decor


@df_decor(start=5)
def get_sum(a):
    return sum(map(int, a.split()))


digs = '5 6 3 6 -4 6 -1'
print(get_sum(digs))