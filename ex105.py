s = set(map(str, input().split()))
lst = []
for x, d in enumerate(s):
    for g, u in enumerate(d):
        if u.isdigit():
            lst.append(u)

a = set(lst)
b = sorted(list(a))
c = ''.join(b)
if c.isdigit():
    print(*c)
else:
    print('НЕТ')

# Python 3.9.11 - best language!