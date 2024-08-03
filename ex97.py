cities = tuple(map(str, input().split()))
lst = list(cities)

for x in lst:
    if x == 'Ульяновск':
        lst.remove(x)
new = (lst)

print(*new)
# Воронеж Самара Тольятти Ульяновск Пермь