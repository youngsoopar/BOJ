a, b = map(int, input().split())
numbers = list(map(int, input().split()))
A = a * b
print(numbers[0]-A, numbers[1]-A, numbers[2]-A, numbers[3]-A, numbers[4]-A,)

# for 문을 이용한 풀이
# L, P = map(int, input().split())
# news = list(map(int, input().split()))
# for i in news:
#     print(i - L * P, end = ' ')