def check_password(password, chars='$%!?@#'):
    """
    Объявите функцию с именем check_password, которая принимает аргумент - строку (пароль) и имеет один формальный параметр chars
    с начальным значением в виде строки "$%!?@#". Функция должна проверять: есть ли в пароле хотя бы один символ из chars и что длина
    пароля не менее 8 символов. Если проверка проходит, то функция возвращает True, иначе - False.

    P. S. Вызывать функцию не нужно, только объявить.
    :param password: строка пароля
    :param chars: '$%!?@#'
    :return: True or False
    """
    if len(password) <= 8:
        return False
    else:
        for x in range(len(password)):
            while x == len(password) - 1:
                print(password[x]) # для тестирования
                if password[x] in chars:
                    return True
                else:
                    return False


# вызываю функцию для тестирования
str = check_password('12345678!')
print(str)