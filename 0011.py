resault = []
for i in range(10) :
    inp = int(input())
    tmp = inp % 42
    if tmp not in resault :
        resault.append(tmp)
print(len(resault))