import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# здесь продолжайте программу (используйте список lst_in)
string_matrix = len(lst_in[0])
flag = True
lst_in = [[0]*string_matrix] + (lst_in) + [[0]*string_matrix] # Добавляем строки вверх и вниз матрицы
for i in range(len(lst_in)): # Добавляем столбцы
    lst_in[i].insert(0, 0) # Первый столбец матрицы
    lst_in[i].append(0) # Последний столбец матрицы
for index_str, value in enumerate(lst_in): # Прохожу по строкам и сохраняю данные в переменную value, индексы index_str
    if flag == True: # Ставлю флаг в True
        for index_positon, value_str in enumerate(value): # Ставлю флаг в True
            if value_str == 1: # Если встречаю 1 в матрице начинаю проверять на соприкосновение с другими единицами
                if (lst_in[index_str][index_positon + 1] == 1 or lst_in[index_str][index_positon - 1] == 1):# Слева или справа
                    flag = False
                    break
                if 1 in lst_in[index_str - 1][index_positon - 1: index_positon +1]: # Верхний ряд
                    flag = False
                    break
                if 1 in lst_in[index_str + 1][index_positon - 1: index_positon +1]: # Нижний ряд
                    flag = False
                    break
                    # Случае нахождения прерываю поиск, flag ставлю в False
                else:
                    flag = True # Иначе flag = True
    else:
        break  # Если флаг в положение False прерываю поиск.
if flag:
    print("ДА")
else:
    print("НЕТ")

#1 0 0 0 0
#0 0 1 0 1
#0 0 0 0 0
#0 1 0 1 0
#0 0 0 0 0