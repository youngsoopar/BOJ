a = input()
lst = ['a','e','i','o','u']
result = 0
for i in range(len(lst)):
    result += a.count(lst[i])

print(result)