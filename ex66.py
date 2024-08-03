number_lst = list(map(int, input().split())) # Записываю данные в список
count = 1 # Создаю счётчик для того чтобы повторно не повторять уже обработанные индексы
#print(number_lst)
for index_1 in range(0, len(number_lst)):          # Беру первое число
    for index_2 in range(count, len(number_lst)):  # Беру второе число
        number_1 = number_lst[index_1]             # Сохраняю первое число
        number_2 = number_lst[index_2]             # Сохраняю второе число
        # Сравнение можно было производить if number_lst[index_1] > [index_2]
        if number_1 > number_2:                    # Если number_1 меньше number_2
            number_mid = number_lst[index_1]       # Сохраняю первое число в промежуточную переменную
            number_lst[index_1] = number_lst[index_2] # Заменяю число в списке на меньшее
            number_lst[index_2] = number_mid       # Переставляю большее число для дальнейшей проверки
            # number_lst[index_1], number_lst[index_2] = number_lst[index_2], number_lst[index_1] # Короткий способ замены значений
    count += 1         # Увеличиваю счетчик на 1 при каждой итерации чтобы не проверять уже замененные значения
print(*number_lst)     # Вывожу результат в консоль

# 8 11 -53 2 10 11