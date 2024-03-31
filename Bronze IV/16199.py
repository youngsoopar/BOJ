birth_day = list(map(int, input().split()))
now = list(map(int, input().split()))
# 만나이 계산
isBirthdaypassed = False
if(now[1] > birth_day[1]):
    isBirthdaypassed = True
elif (now[1] == birth_day[1]):
    if(now[2]>= birth_day[2]):
        isBirthdaypassed = True
    else:
        isBirthdaypassed = False
else:
    isBirthdaypassed = False

if (isBirthdaypassed == True):
    print(now[0]- birth_day[0])
else:
    print(now[0] - birth_day[0] - 1)

# 한국 나이 계산
print(now[0]-birth_day[0]+1)

# 연나이
if now[0] == birth_day[0]:
    print(0)
else:
    print(now[0] - birth_day[0])
