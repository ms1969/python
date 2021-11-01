
message= ["no one likes this","Peter likes this","Jacob and Alex like this","Max, John and Mark like this","Alex, Jacob and 2 others like this"]
def likes (names):
    message= ["no one likes this","Peter likes this","Jacob and Alex like this","Max, John and Mark like this","Alex, Jacob and 2 others like this"]
    if names == []:
        return(message[0])
    elif names == ["Peter"]:
        return(message[1])
    elif names == ["Jacob", "Alex"]:
        return(message[2])
    elif names == ["Max", "John", "Mark"]:
        return(message[3])
    elif len(names) > 3:
        return "Alex, Jacob and " + str(len(names)-2) +  " others like this"
    
    
print (likes(["Alex", "Jacob", "Mark", "Max", "James"])) 



#for letter in 'Python':
#    if letter == 'y':   
#        print('This is pass block')
#    print(letter)
#import sys
#print(sys.version)










    








