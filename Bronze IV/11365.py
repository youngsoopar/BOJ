while True:
    A = input()
    if A == 'END':
        break
    B = list(A)
    print(''.join(B[::-1]))