x = input()
while True:
    if int(x) == int(x[0])*len(x):
        print('FA')
        break
    x = str(int(x[0])*len(x))
else:
    print('NFA')


# 근데 모든수가 FA라 그냥 print('FA') 해도 맞음.