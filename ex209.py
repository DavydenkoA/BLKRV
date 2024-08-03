'''
Подвиг 5. На вход программе подается строка с email-адресами, записанных через пробел. Нужно прочитать эту строку и
среди email-адресов оставить только корректно записанные адреса. Полагается, что к таким относятся те, что используют
только латинские буквы, цифры и символ подчеркивания. Также в адресе должен быть символ "@", а после него символ
точки "." (между ними, конечно же, могут быть и другие символы).
Результат отобразить в виде строки email-адресов, записанных через пробел в порядке их следования в исходной строке.
Тесты: https://github.com/selfedu-rus/test-python-base/tree/main/9/9.4.5
Sample Input:
abc@it.ru dfd3.ru@mail biba123@list.ru sc_lib@list.ru $fg9@fd.com
Sample Output:
abc@it.ru biba123@list.ru sc_lib@list.ru
'''
# Определяем функцию is_valid_email, которая принимает email и возвращает True, если email валидный, и False в противном случае
def is_valid_email(email):
    # Приводим email к нижнему регистру и проверяем, что символ "@" встречается до символа "."
    email = email.lower()
    if email.find("@") >= email.find("."):
        return False
    # Проверяем, что все символы в email принадлежат допустимому набору символов
    for i in email:
        if i not in "abcdefghijklmnopqrstuvwxyz1234567890_@.":
            return False
    # Если email проходит все проверки, возвращаем True
    return True
# Читаем строку ввода, разбиваем ее на слова и фильтруем список слов, оставляя только валидные email
valid_emails = filter(is_valid_email, input().split())
# Выводим список валидных email, разделяя его элементы пробелами
print(*valid_emails)
