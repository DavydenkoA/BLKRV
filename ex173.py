'''
Подвиг 2. На вход программы поступает строка с названиями пунктов меню, записанные в одну строчку через пробел.
В программе реализовано чтение этой строки командой:
menu = input()
Необходимо задать функцию с именем get_menu с сигнатурой:
def get_menu(s): ...
которая преобразует переданную ей строку s в список из слов и возвращает этот список.
Определите декоратор для этой функции с именем show_menu, который отображает список на экран в формате:
1. Пункт_1
2. Пункт_1
...
N. Пункт_N
Примените декоратор show_menu к функции get_menu, используя оператор @. Более ничего в программе делать не нужно.
Сами функции не вызывать.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/7/7.11.2
Sample Input:
Главная Добавить Удалить Выйти
Sample Output:
1. Главная
2. Добавить
3. Удалить
4. Выйти
'''

def show_menu(func):
    def wrapper(*args): # функция, которая выполняет блок команд
        menu = func(*args) # запускаем оборачиваемую функцию
        [print(f"{i + 1}. {j}") for i, j in enumerate(menu)] # выводим результат согласно задания
    return wrapper # возвращаем результат блока команд (запускаем)


@show_menu # применяем декоратор
def get_menu(s): # объявляем функцию
    return s.split() # превращаем в список

menu = 'Главная Добавить Удалить Выйти'
print(get_menu(menu))

