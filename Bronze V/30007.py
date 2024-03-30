A = int(input())
for i in range(A):
    a, b, c = map(int, input().split())
    print(a*(c-1)+b)