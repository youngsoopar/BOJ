A, B = map(int,input().split())
c = list(map(int, input().split()))

for i in range(A):
    if c[i] < B:
        print(c[i], end = ' ')