max = sum(list(map(int,input().split())))
cur = 1
for i in range(2,5+1) :
    tmp = sum(list(map(int,input().split())))
    if max < tmp :
        max = tmp
        cur = i
print(cur,max)