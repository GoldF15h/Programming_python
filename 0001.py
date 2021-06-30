a = 0
for i in range(3):
    a += int(input())

if a  <= 49 :
    print('F')
elif a <= 54 :
    print('D')
elif a <= 59 :
    print('D+')
elif a <= 64 :
    print('C')
elif a <= 69 :
    print('C+')
elif a <= 74 :
    print('B')
elif a <= 79 :
    print('B+')
else :
    print('A')
