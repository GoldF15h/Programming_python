month = [4,0,0,3,5,1,3,6,2,4,0,2]
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
d,m = map(int,input().split())
date = day[ ( month[m-1]+d-1 )%7 ]
print(date)