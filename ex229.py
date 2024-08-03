'''
Подвиг 1. На вход программе подаются целые числа, записанные через пробел. Необходимо их прочитать и определить,
являются ли все эти числа четными. Вывести True, если это так и False в противном случае.
Задачу реализовать с использованием одной из функций: any или all.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.9.1
Sample Input:
2 4 6 8 22 56
Sample Output:
True
'''
#a = list(map(int, input().split()))
a = [2, 4, 6, 8, 22, 56]
print(all(map(lambda x: x % 2 == 0, a)))