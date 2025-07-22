N, X = map(int, input().split())
A = list(map(int, input().split()))

for _a in A:
    if _a < X:
        print(_a, end=' ')