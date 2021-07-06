n = input()
s3 , s11 = 0,0

tmp = 0
for i in n :
    tmp = tmp + int(i)
    tmp = tmp % 3
    tmp = tmp * 10

print(tmp//10,end=' ')

tmp = 0
for i in n :
    tmp = tmp + int(i)
    tmp = tmp % 11
    tmp = tmp * 10

print(tmp//10,end='')
