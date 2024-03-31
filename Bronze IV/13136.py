R, C, N = map(int, input().split())

if R % N == 0:
    A = R//N
else:
    A = R//N +1
if C % N == 0:
    B = C//N
else:
    B = C//N +1
print(A*B)

# R, C, N = map(int, input().split())
# a = R//N + 1 if R%N else R//N
# b = C//N + 1 if C%N else C//N
# print(a*b)
#  컴프리헨션?
