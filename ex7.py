a, b, c, d = map(int, input().split())
if (a-2) >= c and (b-2) >= d or (a-2) >= d and (b-2) >= c:
    print('ДА')
else:
    print('НЕТ')


# 12 5 7 2