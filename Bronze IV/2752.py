a, b, c = map(int, input().split())
num_list = []
num_list.append(a)
num_list.append(b)
num_list.append(c)

num_list.sort()
print(num_list[0], num_list[1], num_list[2])