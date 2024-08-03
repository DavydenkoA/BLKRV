'''
Подвиг 6. На вход программе подается строка с именами студентов, записанными через пробел. Требуется прочитать
эти имена и случайным образом выбрать трех студентов из этого списка, используя функцию sample. (Полагается, что
в исходном списке более трех студентов). Результат вывести на экран в одну строчку через пробел.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/10/10.3.6
Sample Input:
Петров Иванов Сидоров Балакирев Фридман
Sample Output:
Иванов Петров Фридман
'''
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
#names = input().split()
names = ['Петров', 'Иванов', 'Сидоров', 'Балакирев', 'Фридман']
three = random.sample(names, 3)
print(*three)