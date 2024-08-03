'''
Подвиг 2. Объявите в программе функцию с именем get_add следующей сигнатуры:
def get_add(a, b): ...
Функция должна складывать или два числа или две строки (но не число со строкой) и возвращать полученный результат.
Если сложение не может быть выполнено, то функция возвращает значение None.
Вызывать функцию не нужно, только объявить. Также ничего не нужно выводить на экран.
Подсказка: не забудьте про необходимость различения булевых значений (False, True) от целочисленных.
'''
def get_add(a, b):
    if type(a) in (int, float) and type(b) in (int, float):
        return a + b
    if isinstance(a, str) and isinstance(b, str):
        return a + b


a = 9.5
b = 8
print(get_add(a, b))