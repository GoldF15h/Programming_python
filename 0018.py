import sys

n,k = map(int,input().split())
l = []
for i in range(2,n+1) :
    l.append(i)
counter = 0
while len(l) != 0 :
    prime = l[0]
    i = 1
    while prime*i <= max(l) :
        if prime*i in l :
            l.remove(prime*i)
            counter = counter + 1
            if counter == k :
                print(prime*i)
                sys.exit()
        i = i + 1