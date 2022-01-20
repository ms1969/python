def main(s):
    lstack = []
    isOk = True
    for i in s:

        if i in '{([':
            lstack.append(i)
            continue
        elif i in ')}]' and len(lstack) !=0:
            s1 = lstack.pop()
            if s1 != i:
                isOk = False
                break
            else:
                continue
    return isOk

if __name__ == '__main__':
    # s = input()
    if main(s):
        print('YES')
    else:
        print('NO')

