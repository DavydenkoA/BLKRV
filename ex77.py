lst_1 = list(map(str, input().split()))
year = [int(lst_1[i]) for i in range(1, len(lst_1), 2)]
town = [str(lst_1[i]) for i in range(0, len(lst_1), 2)]
lst = [[town[x]]+[year[x]] for x in range(len(year))]
print(lst)

# Москва 15000 Уфа 1200 Самара 1090 Казань 1300