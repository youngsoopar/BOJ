A = input()

for i in A:
    if i.isupper() == True:
        print(i.lower(), end ='')
    else:
        print(i.upper(), end ='')
