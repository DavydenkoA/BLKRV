def verify(lst):
    new_lst = []
    new_lst_elem = []
    for i in range(len(lst) - 1):
        for k in range(len(lst)):
            new_lst_elem.append(lst[i][k] + lst[i + 1][k])
        new_lst.append(''.join(map(str, new_lst_elem)))
        new_lst_elem = []
    for elem in new_lst:
        if '11' in elem or '2' in elem:
            return False
    return True


#verify([[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]])