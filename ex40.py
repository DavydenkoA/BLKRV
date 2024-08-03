n = int(input())
km = 10
day = 1
while km <= n:
    km += km / 100 * 10
    day += 1
else:
    print(day)