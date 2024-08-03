lst = list(map(str, input().split()))
firstLtr = 0
secondLtr = - 1
i = 0
lstLen = len(lst)
for x in range((lstLen) - 1):
        if str.lower(lst[x][secondLtr]) == "ь" or str.lower(lst[x][secondLtr]) == "ъ" or str.lower(lst[x][secondLtr]) == "ы":
            secondLtr = -2
        if str.lower(lst[x][secondLtr]) == str.lower(lst[(x + 1)][firstLtr]):
            i += 1
        secondLtr = -1
if i == lstLen - 1:
    print("ДА")
else:
    print("НЕТ")



# Москва Астрахань Новгород Димитровград Душанбе