'''
Подвиг 4. На вход программе подаются оценки студента, записанные через пробел. Необходимо их прочитать и определить,
имеется ли в этом списке хотя бы одна оценка ниже тройки. Если это так, то вывести на экран строку "отчислен",
иначе - "учится".
Задачу реализовать с использованием одной из функций: any или all.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.9.4
Sample Input:
3 3 3 2 3 3
Sample Output:
отчислен
'''
#a = list(map(int, input().split()))
def get_stude(lst):
    z = any(map(lambda x: x < 3, lst))
    if z == True:
        return 'отчислен'
    else:
        return 'учится'

a = [3, 3, 3, 2, 3, 3]
print(get_stude(a))