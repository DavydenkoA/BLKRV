cities = list(map(str, input().split()))
s = []
for x in cities:
    s.append(len(x))
print(*s)

# Москва Уфа Караганда Тверь Минск Казань