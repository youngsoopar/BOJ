year = int(input())

if year % 400 == 0 : # 400의 배수일떄
    print(1)
elif year % 4 == 0 and year % 100 != 0: # 4의 배수이면서, 100의 배수가 아닐때
    print(1)
else:
    print(0)
