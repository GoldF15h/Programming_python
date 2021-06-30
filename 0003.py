m,n = map(int,input().split())
matrix = [[]]*m
for i in range(m) :
    matrix[i] = list(map(int,input().split()))
for i in range(m) :
    tmp = list(map(int,input().split()))
    for j in range(n) :
        matrix[i][j] = matrix[i][j] + tmp[j]
for i in range(m) :
    print(' '.join( str(x) for x in matrix[i] ))