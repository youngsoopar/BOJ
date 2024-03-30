a = int(input())
b = int(input())
c = int(input())

d= f'{a*b*c}'
for i in range(10):
    print(d.count(str(i)))