N = int(input())
for x in range(N):
    for h in range(1, N):
        if h >= 0:
            print(1, end=' ')
        if h == N - 1:
            print(5, end='')
    print()
