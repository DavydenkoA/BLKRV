'''
Значимый подвиг 4. Имеется таблица с данными, представленная в формате:
Номер;Имя;Оценка;Зачет
1;Иванов;3;Да
2;Петров;2;Нет
...
N;Балакирев;4;Да
 В программе уже реализовано их считывание в список lst_in:
lst_in = list(map(str.strip, sys.stdin.readlines()))
Данные этого списка необходимо разбить по разделителю ";" и представить в виде двумерного (вложенного) кортежа
в формате:
( ('Номер', 'Имя', 'Оценка', 'Зачет'), (1, 'Иванов', 3, 'Да'), (2, 'Петров', 2, 'Нет'), ... )
При этом все числа должны быть представлены как целые числа. Затем, отсортировать этот кортеж так, чтобы столбцы шли
в порядке:
Имя;Зачет;Оценка;Номер
Реализовать эту операцию с помощью сортировки. Результат должен быть представлен также в виде двумерного кортежа и
присвоен переменной с именем t_sorted.
Программа ничего не должна выводить на экран, только формировать двумерный кортеж с переменной t_sorted.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.7.4
Sample Input:
Номер;Имя;Оценка;Зачет
1;Портос;5;Да
2;Арамис;3;Да
3;Атос;4;Да
4;д'Артаньян;2;Нет
5;Балакирев;1;Нет
Sample Output:
True
'''
import sys
# считывание списка из входного потока (не меняйте переменную lst_in в программе)
#lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = ['1;Портос;5;Да', '2;Арамис;3;Да', '3;Атос;4;Да', "4;д'Артаньян;2;Нет", '5;Балакирев;1;Нет']
# здесь продолжайте программу (используйте список строк lst_in)
# функция для извлечения нужных данных и преобразования их в нужный формат
def g(list):
    # разбиение строки на элементы по разделителю ";"
    x = list.split(";")
    # проверка, что первый являются числами
    if (x[0].isdigit()):
        # возвращение элементов в нужном порядке и в нужном формате
        return x[1], x[3], int(x[2]), int(x[0])
    else:
        # возвращение элементов в нужном порядке и в нужном формате
        return x[1], x[3], x[2], x[0]
# преобразование исходного списка в двумерный кортеж с помощью функции g
t_sorted = tuple([tuple(g(i)) for i in lst_in])