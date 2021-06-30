n = int(input())
w = n-1 if n%2==0 else n
h = n

for i in range((n+1)//2) :
    op = ''
    for j in range(w) :
        if abs( j+1 - (w+1)/2 ) ==  i :
            op = op + '*'
        else:
            op = op + '-'
    print(op)

for i in range( (n//2)-1,0-1,-1 ) :
    op = ''
    for j in range(w) :
        if abs( j+1 - (w+1)/2 ) ==  i :
            op = op + '*'
        else:
            op = op + '-'
    print(op)