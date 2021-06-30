def scoring (st,pattern):
    score = 0
    for i in range(len(st)) :
        if st[i] == pattern[i%len(pattern)] :
            score = score + 1
    return score

sc = int(input())
st = input()
op = []
op.append( scoring(st,'ABC'))
op.append( scoring(st,'BABC'))
op.append( scoring(st,'CCAABB'))

print(max(op))
if op[0] == max(op) :
    print('Adrian')
if op[1] == max(op) :
    print('Bruno')
if op[2] == max(op) :
    print('Goran')

