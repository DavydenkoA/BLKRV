cities = tuple(map(str, input().split()))
msc = ('Москва',)
if msc[0] not in cities:
    cities += msc

print(*cities)

# Уфа Казань Самара