n = int(input ("Введите количество раундов: "))
m = 0
c = 0
for i in range(1, n+1):
    s =input ("Введите результат попытки: ")
    k =  s.split()
    mR  = int(k[0])
    cR  = int(k[1])
    if mR > cR:
        m += 1
    elif cR > mR:
        c += 1
if m > c:
    print ("Mishka")
elif c > m:
    print ("Chris")
else:
    print ("Friendship is magic!^^")
    








    








