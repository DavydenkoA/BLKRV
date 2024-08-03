first = set(map(str, input().split()))
second = set(map(str, input().split()))

s = first & second
if s == first:
    print('ДА')
else:
    print('НЕТ')




# Москва Казань Самара Москва
# Москва Владимир Новгород Казань Самара Москва