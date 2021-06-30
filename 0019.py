def possible (l,n,current=0,mix=[]):
    if current < n :
        mix.append(l[current])
        a = possible(l,n,current+1,mix)
        mix.remove(l[current])
        b = possible(l,n,current+1,mix)
        return min(a,b)
    else :
        if len(mix) != 0 :
            sweet = 1
            sour = 0
            for i in mix :
                sweet = sweet*i[0]
                sour = sour+i[1]
            return abs(sweet - sour)
        else :
            return 10000000
        
n = int(input())
l = []
for i in range(n) :
    l.append( list(map(int,input().split())) )
print(possible(l,n))