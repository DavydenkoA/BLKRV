a = list(map(str, input().split()))
if 'Москва' in a:
    a.remove('Москва')
print(*a)

#print(*a)

# Уфа Астрахань Москва Самара Казань