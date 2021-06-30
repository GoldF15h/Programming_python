a,b = map(int,input().split())
while b != 0 :
    a = a % b 
    a,b = b,a 
print(a)