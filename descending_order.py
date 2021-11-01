
def descending_order(num):
    nList = []
    sNum = str(num)
    for item in range(0, len(str(num))):
        nList.append(sNum[item])
    nList.sort()
    sNum = ''
    for item in range(0, len(str(num))):
        sNum = sNum + str((nList.pop()))
    return int(sNum)

print (descending_order(13409578110))


    













    








