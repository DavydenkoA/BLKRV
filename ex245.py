'''
Подвиг 5. На вход программе подается таблица целых чисел, записанных через пробел. В уже программе реализовано
чтение ее строк:
lst_in = list(map(str.strip, sys.stdin.readlines()))
Необходимо преобразовать список строк lst_in в двумерный список чисел. Затем, в полученном списке (таблице)
перемешать столбцы, используя функции shuffle и zip. Результат вывести на экран (также в виде таблицы).
При выводе в конце строк не должно быть пробелов.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.5
Sample Input:
1 2 3 4
5 6 7 8
9 8 6 7
Sample Output:
4 1 3 2
8 5 7 6
7 9 6 8
'''
import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['1 2 3 4', '5 6 7 8', '9 8 6 7']
# здесь продолжайте программу
# создание списка из столбцов таблицы
lst = list(zip(*map(str.split, lst_in)))
# перемешивание столбцов
random.shuffle(lst)
# вывод на экран перемешанной таблицы
for row in zip(*lst):
    print(*row)