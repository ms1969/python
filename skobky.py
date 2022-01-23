def main(s):
    lstack = []
    isOk = True
    for i in s:
        if i in '{([':
            lstack.append(i)
        elif i in ')}]' and len(lstack) != 0:
            if i == ')' and '(' in lstack:
                lstack.remove('(')
            elif i == '}' '{' in lstack:
                lstack.remove('{')
            elif i == ']' '[' in lstack:
                lstack.remove('[')
            elif i in ')}]':
                isOk = False
                break
        elif i in ')}]' and len(lstack) == 0:
            isOk = False
            break
    return isOk


if __name__ == '__main__':
    s = input('Введите строку: ')
    if main(s):
        print('YES')
    else:
        print('NO')
