def get_str(a):
    return a, len(a)

lst = []
#d = {}
cities = list(map(str, input().split()))

for i in cities:
    lst.append(get_str(i))

d = dict(lst)
a = sorted(d, key=lambda x: d[x])
print(*a)


# Воронеж Лондон Тверь Омск Уфа