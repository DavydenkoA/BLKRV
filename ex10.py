m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''
lst = list(m.split('\n'))
num = int(input())
if num == 1:
    print(lst[0])
elif num == 2:
    print(lst[1])
elif num == 3:
    print(lst[2])
elif num == 4:
    print(lst[3])
elif num == 5:
    print(lst[4])
elif num == 6:
    print(lst[5])
