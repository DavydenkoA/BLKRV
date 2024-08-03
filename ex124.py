def vvod():
    lst_in = list(map(int, input().split()))
    lst_in.sort()
    print(f"Min = {lst_in[0]}, max = {lst_in[-1]}, sum = {sum(lst_in)}")


vvod()




# 8 11 5 -10 12 0