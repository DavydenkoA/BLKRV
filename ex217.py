'''
Подвиг 4. На вход программе поступают целые числа, записанных через пробел. Необходимо их прочитать и выбрать из
них четыре наибольших уникальных значения. Результат вывести на экран в порядке их убывания в одну строчку через пробел.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.6.4
Sample Input:
10 5 4 -3 2 0 5 10 3
Sample Output:
10 5 4 3
'''

digs = list(map(int, '10 5 4 -3 2 0 5 10 3'.split()))
digs.sort(reverse=True)
dic = dict.fromkeys(digs)
lst = list(dic.keys())
print(*lst[:4])