def get_biggest_city(*args):
    return max(args, key=lambda i: len(i))


get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж')

