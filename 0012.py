inp = input()
inp_len = len(inp)

print('..#..',end='')
for j in range(2,inp_len+1) :
    if j % 3 == 0 :
        print('.*..',end='')
    else :
        print('.#..',end='')
print()

print('.#.#.',end='')
for j in range(2,inp_len+1) :
    if j % 3 == 0 :
        print('*.*.',end='')
    else :
        print('#.#.',end='')
print()

print('#.{}.#'.format(inp[0]),end='')
for j in range(2,inp_len+1) :
    print('.{}.'.format(inp[j-1]),end='')
    if j != inp_len :
        if ( ( j + 1 ) % 3 == 0 or j % 3 == 0 ) :
            print('*',end='')
        else :
            print('#',end='')
    else :
        if inp_len % 3 == 0 :
            print('*',end='')
        else :
            print('#',end='')
print()

print('.#.#.',end='')
for j in range(2,inp_len+1) :
    if j % 3 == 0 :
        print('*.*.',end='')
    else :
        print('#.#.',end='')
print()

print('..#..',end='')
for j in range(2,inp_len+1) :
    if j % 3 == 0 :
        print('.*..',end='')
    else :
        print('.#..',end='')
print()
