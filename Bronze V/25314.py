A = int(input())
if A % 4 == 0:
    print(A//4 * 'long '+"int")
else:
    print((A//4 +1) * 'long '+'int')