K,Q,L,B,N,P = map(int, input().split())
chess = []
A = [K,Q]
B = [L,B,N]
C = [P]
for i in A:
    one = i -1
    chess.append(-one)

for j in B:
    two = j -2
    chess.append(-two)

for l in C:
    eight = l -8
    chess.append(-eight)

print(*chess, sep=' ')