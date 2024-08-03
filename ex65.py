import sys
# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
# здесь продолжайте программу (используйте список lst_in)
flag = True # Создаю флаг
count = 1 # Счетчик для начала второго индекса
# for index, value in enumerate(lst_in): # Для отрисовки матрицы
#     print(value)
# for index_1, value_1 in enumerate(lst_in):
for index_1 in range(0, len(lst_in)): # Получения первой части индекса (Основной список)
    for index_2 in range(count, len(lst_in)): # Получения второй части индекса (Вложенный список)
        # if lst_in[index_1][index_2] != lst_in[index_2][index_1]: # Сокращенный вариант проверки
        number_1 = lst_in[index_1][index_2] # Сохраняю число из массива стоящее слева
        number_2 = lst_in[index_2][index_1] # Сохраняю число из массива стоящее справа
        if number_1 != number_2: # Проверяю их на неравенство
            flag = False # Если они не равный то условия нашего задания не исполняются и можно выходить из цикла flag = False
            break   # Прерываю работу цикла с помощью break
        else: # Если равны то устанавливаю флаг на True и продолжаю проверку
            flag = True
    if flag == False: # Если Флаг равен False то выхожу из внешнего цикла
        break
if flag: # Если Флаг равен True то печатаю ДА
    print("ДА")
else:   # Если Флаг равен False то печатаю НЕТ
    print("НЕТ")


#2 3 4 5 6
#3 2 7 8 9
#4 7 2 0 4
#5 8 0 2 1
#6 9 4 1 2