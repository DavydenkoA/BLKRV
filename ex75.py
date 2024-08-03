num_list = input().split() # Пользовательский ввод
num_index = [num_list[num] for num in range(0, len(num_list)) if float(num) % 2 == 0] # Выбираю элементы по индексу
# если он идут под четными индексами в списке
print(*num_index)

# 8.5 11.3 1.0 -4.5 11.34 6.45