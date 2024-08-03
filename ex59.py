stroka = input()
a = iter(stroka)
lst = ['']
while lst[-1] != ' ':
    lst.append(next(a))
print(''.join(lst))


# Возможно-это будет полезно