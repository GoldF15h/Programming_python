l = list(map(int,input().split()))
l.sort()
# print(l)
st = input()
for i in range(3) :
    if st[i] == 'C' :
        print(l[2],end =' ')
    elif st[i] == 'B' :
        print(l[1],end =' ')
    else :
        print(l[0],end =' ')