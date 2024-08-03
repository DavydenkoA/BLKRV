d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

# здесь продолжайте программу

def get_line_list(d,a=[]):
    for x in d:
        if type(x) != list:
            a.append(x)
        else:
            get_line_list(x)
    return a


get_line_list(d)

print(get_line_list(d))