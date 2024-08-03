'''
Подвиг 4. На вход программе подается строка в формате:
ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
Необходимо ее прочитать и с помощью функции map преобразовать ее в кортеж tp вида:
tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.3.4
Sample Input:
house=дом car=машина men=человек tree=дерево
Sample Output:
True
'''
# ввод строки (переменную s не менять)
#s = input()
s = 'house=дом car=машина men=человек tree=дерево'
s_lst = s.split()

# здесь продолжайте программу
tp = tuple((tuple(map(str, i.split("="))) for i in s_lst))
for i in tp:
    print(i,end='')