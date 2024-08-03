
#a, b = map(float, input().split())
#a = list(map(int, input().split()))
a = list(input(). casefold()) #не учитываем регистр
b = a[::-1]
if a == b:
    print('ДА')
else:
    print('НЕТ')

