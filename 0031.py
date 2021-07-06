l = list(map(int,input().split()))
count = 0
while sum(l) != 3 :
    m = max(l)
    for i in range(3) :
        if l[i] == m :
            if l[i] % 2 == 0 :
                l[i] = l[i] /2
            else :
                l[i] = (l[i]-1)/2
            count = count + 1
print(count)
    