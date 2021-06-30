inp = input()
ignore = ['a','e','i','o','u']
i = 0
while i < len(inp) :
    print(inp[i],end='')
    if inp[i] in ignore :
        i = i + 3
    else :
        i = i + 1