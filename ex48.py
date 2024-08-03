m = int(input())
for x in range(2, m):
    if m % x == 0:
        print('НЕТ')
        break
else:
        print('ДА')