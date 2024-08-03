'''
Подвиг 5. На вход программе подается текущее игровое поле для игры "Крестики-нолики" в виде следующей таблицы
(списка строк):
# x o
x # x
o o #
Здесь # - свободная клетка. В программе уже реализовано чтение этих строк и сохранение в список lst_in:
lst_in = list(map(str.strip, sys.stdin.readlines()))
Необходимо преобразовать этот список строк в двумерный список с именем pole вида (пример):
[ ['#', 'x', 'o'], ['x', '#', 'x'], ['o', 'o', '#'] ]
Объявите в программе функцию с именем is_free сигнатуры:
def is_free(lst): ...
На вход этой функции подается игровое поле в виде двумерного (вложенного) списка. Данная функция должна возвращать
True, если есть хотя бы одна свободная клетка и False в противном случае.
Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран. Задачу реализовать с
использованием одной из функций: any или all.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.9.5
'''
import sys
# считывание списка из входного потока (переменную lst_in не менять)
#lst_in = list(map(str.strip, sys.stdin.readlines()))
# здесь продолжайте программу (используйте список строк lst_in)
def is_free(lst):
    asw = []
    for x in lst:
        for g in x:
            if '#' in g:
                asw.append(True)
            else:
                asw.append(False)
    return any(asw)


lst_in = ['# x o', 'x # x', 'o o #']
pole = list(map(lambda x: [x], lst_in))

print(is_free(pole))