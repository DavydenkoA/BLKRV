lst_in = list(map(int,input().split()))
size_matrix = int(len(lst_in) ** 0.5)
result = [[lst_in[size_matrix * i + j] for j in range(size_matrix)] for i in range(size_matrix)]
print(result)

# 1 2 3 4 5 6 7 8 9