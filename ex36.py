cities = input().split()
e = len(cities)
count = 0
while count < e:
    len_cities = len(cities[count])

    if len_cities < 5:
        print('НЕТ')
        break
    count +=1
else:
    print('ДА')



# Самара Ульяновск Новгород Воронеж