cities = input()
a = [city for city in cities.split() if len(city) > 5]
print(*a)

# Казань Уфа Москва Челябинск Омск Тур Самара