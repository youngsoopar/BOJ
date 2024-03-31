A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
P = [A,B,C]

for i in range(len(P)):
    if P[i][5] - P[i][2] < 0:
        P[i][4] -= 1
        P[i][5] += 60
    if P[i][4] - P[i][1] < 0:
        P[i][3] -= 1
        P[i][4] += 60
    print((P[i][3] - P[i][0]), (P[i][4] - P[i][1]), (P[i][5] - P[i][2]))