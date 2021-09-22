def tickets(people):
    n25, n50 = 0, 0
    for item in people:
        if item == 25:
            n25 += 25
        elif item == 50 and (n25 // 25 == 0): 
            return 'NO'
        elif item == 50 and (n25 // 25 > 0): 
            n50 += 50
            n25 -= 25
        elif item == 100 and ((n25 + n50) // 75 == 0) or n25 // 25 == 0:
            return 'NO'
        elif item == 100 and ((n25 + n50) // 75 > 0):
            if n50 // 50 > 0:
                n50 -= 50
                n25 -= 25
            else:
                n25 -= 75
    return 'YES'     

people = [25, 25, 50, 50, 100]    
print (tickets(people))














    








