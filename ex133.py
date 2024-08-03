def get_str(a):
    if len(a) < 6:
        return False
    else:
        return True


lst = []
cities = list(map(str, input().split()))

for i in cities:
    if get_str(i):
        lst.append(i)
    else:
        continue

print(*lst)

# Москва Уфа Пермь Самара Вологда