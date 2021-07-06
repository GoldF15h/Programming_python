jump , dis = map(int,input().split())
i = 0
if dis < jump :
    print(2)
elif dis % jump == 0 :
    print(dis // jump)
else :
    print(dis // jump + 1)