'''
Значимый подвиг 7. В программе инициализируется двумерное игровое поле размером N x N (N - натуральное число
читается из входного потока), представленное в виде вложенного списка:
P = [[0] * N for i in range(N)]
Требуется расставить на поле P случайным образом M = 10 единиц (целочисленных) так, чтобы они не соприкасались друг
с другом (то есть, вокруг каждой единицы должны быть нули, либо граница поля).
P.S. Поле на экран выводить не нужно (вообще ничего не нужно выводить), только сформировать.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.7
Sample Input:
10
Sample Output:
True
'''
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
#N = int(input())
N = 10
P = [[0] * N for i in range(N)]

# здесь продолжайте программу
k = 0

while k < 10:
    f = random.randint(0, N-1)
    j = random.randint(0, N-1)

    if f % 2 == 0 and j % 2 == 0 and P[f][j] != 1:
        P[f][j] = 1
        k += 1
