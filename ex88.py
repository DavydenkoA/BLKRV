d = {}

while True:
    num = int(input())
    if num == 0:
        break
    if num not in d:
        d[num] = round(num ** 0.5, 2)
        print(d[num])
    else:
        print('значение из кэша:', d[num])