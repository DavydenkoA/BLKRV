number_lst = list(map(int, input().split()))  # Записываю данные в список
count = 0   # Создаю счетчик чтоб проверять два рядом стоящих числа
for index in range(0, len(number_lst)):       # Это цикл задает число проходов по списку
    count = 0                                 # Каждую новую итерация я обнуляю счетчик для прохода с 0 элемента цикла
    for index_2 in range(1, len(number_lst)): # Каждую новую итерация я обнуляю счетчик для прохода с 0 элемента цикла
        # number_1 = number_lst[count]        # Сохраняю первое число
        # number_2 = number_lst[index_2]      # Сохраняю второе число
        # if number_1 > number_2:  # Если number_1 меньше number_2
        if number_lst[count] > number_lst[index_2]: # Если первое значение больше второго
            number_lst[count], number_lst[index_2] = number_lst[index_2], number_lst[count] # Меняем значения местами
        count += 1     # Увеличиваю счетчик на 1 при каждой итерации чтобы не проверять уже замененные значения
print(*number_lst)     # Вывожу результат в консоль

# 4 5 2 0 6 3 -56 3 -1