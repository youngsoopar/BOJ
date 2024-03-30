a,b,c,d,e,f,g,h = map(int, input().split())
doremi = [a,b,c,d,e,f,g,h]

if doremi == [1,2,3,4,5,6,7,8]:
    print('ascending')
elif doremi == [8,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')