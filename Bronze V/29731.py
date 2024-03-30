A = int(input())
B_list = ['Never gonna give you up',"Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]

check = False
for i in range(A):
    i = input()
    if i not in B_list:
        check = True
        break
if check:
    print('Yes')
else:
    print('No')