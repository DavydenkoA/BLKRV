def get_rec_N(N):
    if N > 0:
        get_rec_N(N - 1)
        print(N)

g = get_rec_N(8)
