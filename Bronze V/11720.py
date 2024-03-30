a = int(input())
b = int(input())
sum = 0
while b>0:
    count = 0
    c = b%10
    b //= 10
    sum += c
    count += 1
    if count == a:
        break
print(sum)