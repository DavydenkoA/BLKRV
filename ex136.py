def get_nod(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a


res = get_nod(15, 121050)
print(res) # в задании вывод результата не нужен