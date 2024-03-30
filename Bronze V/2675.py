a = int(input())

for i in range(a):
    r , s = input().split()
    r = int(r)

    b = ''
    for j in s:
        b += j * r
    print(b)