
s = input()
lstack = []
isOk = True
for i in s:
    if i in '{([':
        lstack.append(i)
        continue
    elif i in ')}]' and len(lstack) !=0:
        s1 = lstack.pop()
        if (s1 == '(' and i == ')') or (s1 == '[' and i == ']') or (s1 == '{' and i == '}'):
            continue
        else:
            isOk = False
    else:
        isOk = False
        break
if isOk:
    print('YES')
else:
    print('NO')

    



