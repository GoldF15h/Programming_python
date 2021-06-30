import sys

inp = []
for i in range(9) :
    inp.append(int(input()))
for i in inp :
    for j in inp :
        if sum(inp) - ( i + j ) == 100 :
            inp.remove(i)
            inp.remove(j)
            print('\n'.join( str (x) for x in inp ))
            sys.exit()
            