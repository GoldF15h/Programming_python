cup = [1,0,0]
st = input()
for i in st :
    # print(i)
    if i == 'A' :
        cup[0] , cup[1] = cup[1] , cup[0]
    elif i == 'B' :
        cup[1] , cup[2] = cup[2] , cup[1]
    else :
        cup[0] , cup[2] = cup[2] , cup[0]
for i in range(3) :
    if cup[i] :
        print(i+1)