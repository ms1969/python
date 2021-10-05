def tickets(people):
    till = {100.0:0, 50.0:0, 25.0:0}

    for paid in people:

    till[paid] += 1
    change = paid-25.0
    
    for bill in (50,25):
      while (bill <= change and till[bill] > 0):
        till[bill] -= 1
        change -= bill

    if change != 0:
      return 'NO'
        
  return 'YES'


people = [25, 25, 50, 50, 100]    
print (tickets(people))











sort(a, reversed = True)



    








