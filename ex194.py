'''
Подвиг 1. На вход программе подается натуральное число N. Оно уже читается в программе командой:
N = int(input())
Объявите в программе функцию-генератор с именем get_sum с сигнатурой:
def get_sum(total): ...
которая бы возвращала текущую сумму чисел последовательности длины total = N в диапазоне целых чисел [1; N]
(включительно). То есть, при вызове get_sum в качестве аргумента передается переменная N. В результате должны получить
следующие результаты работы функции-генератора:

при первом вызове get_sum возвращает сумму 1;
при втором вызове get_sum возвращает сумму чисел 1+2 = 3;
при третьем вызове get_sum возвращает сумму чисел 1+2+3 = 6;
....
для N-го вызова get_sum возвращает сумму
1+2+...+(N−1)+N.
Реализовать функцию-генератор get_sum без использования коллекций. Вызывать ее не нужно, только объявить.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.2.1
Sample Input:
5
Sample Output:
1 3 6 10 15
'''

N = int(input())
# Функция-генератор get_sum принимает на вход число N, которое задает длину последовательности, сумму чисел которой нужно вычислить.
def get_sum(N):
    # Начальная сумма равна 0
    current_sum = 0
    # В цикле for проходим по всем числам от 1 до N включительно
    for i in range(1, N+1):
        # Добавляем к текущей сумме текущее число i
        current_sum += i
        # Возвращаем текущую сумму
        yield current_sum