'''
Подвиг 2. На вход программе подается список предметов в виде строк формата:
название_1=вес_1
...
название_N=вес_N
В программе уже реализовано их считывание в список lst_in:
lst_in = list(map(str.strip, sys.stdin.readlines()))
С помощью функции map, необходимо сначала преобразовать этот список строк в кортеж, элементами которого также являются
кортежи, то есть, представить список в формате:
(('название_1', 'вес_1'), ..., ('название_N', 'вес_N'))
А, затем, отфильтровать (исключить) все предметы с весом менее 500, используя функцию filter. Вывести на экран список
оставшихся предметов (только их названия) в одну строчку через пробел в порядке их следования во входных данных.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.2
Sample Input:
зонт=1000
палатка=10000
спички=22
котелок=543
Sample Output:
зонт палатка котелок
'''
import sys

# считывание списка из входного потока
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']
# здесь продолжайте программу (используйте список lst_in)
tup = tuple(map(lambda x: (x[:x.index('=')], x[x.index('=') + 1:]), lst_in))
tup_2 = list(filter(lambda x: int(x[1]) >= 500, tup))
tup_3 = map(lambda x: x[0], tup_2)
print(*tup_3)

