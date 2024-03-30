a = int(input())

for i in range(a):
    b = list(input().split(sep= 'X'))
    c = list(map(len, b))
    d = list(map(lambda x : x*(x+1)//2 ,c))
    print(sum(d))