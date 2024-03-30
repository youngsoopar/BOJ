a, b = map(int, input().split())
chess = []
for i in range(a):
    c = list(input())
    chess.append(c)

if chess[0][0] == 'B':
    while chess[a-1][b-1] == 'B':
        for j in range(a):
            for k in range(b):
                chess[j][k]