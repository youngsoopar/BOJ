L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
if A%C == 0:
    korean = A//C
else:
    korean = A//C + 1
if B%D == 0:
    math = B//D
else:
    math = B//D + 1
print(L-max(korean, math))