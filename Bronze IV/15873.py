N = input()
if len(N) == 4:         # 1010
    print(20)
elif len(N) == 2:       # AB
    print(int(N[0]) + int(N[1]))
else:
    if int(N[-1]) == 0: # A10
        print(int(N[0])+ 10)
    else:               # 10B
        print(int(N[-1])+ 10)