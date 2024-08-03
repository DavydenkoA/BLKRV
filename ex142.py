def get_even(*args):
    lst = []
    for x in args:
        if x % 2 == 0:
            lst.append(x)
    print(*lst) # для правильного решения в задаче return lst


get_even(45, 4, 8, 11, 12, 0)


# 45 4 8 11 12 0