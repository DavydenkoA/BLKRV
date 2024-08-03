def str_min(a, b):
    """Функция возвращает
    минимальную строку из двух
    """
    return min(a, b)
def str_min3(a, b, c):
    """Функция возвращает
    минимальную строку из трех
    """
    return str_min(a, str_min(b, c))
def str_min4(a, b, c, d):
    """Функция возвращает
    минимальную строку из четырех
    """
    return str_min(a, str_min3(b, c, d))




