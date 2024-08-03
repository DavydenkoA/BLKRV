names = input().lower().split()
e = len(names)
count = 0
while count < e:
    if names[count][-1] == names[count][0]:
        print('ДА')
        break
    count +=1
else:
    print('НЕТ')



# Петр Анна Иван Сергей Михаил Федор