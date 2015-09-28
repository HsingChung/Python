#HW03_P1
#HsingChung Wang
#09/25/2015
def bunnyEars(p):
    if p<1: return 0 #if the number of bunnies is smaller than 1
    elif p%2: return bunnyEars(p-1)+2 #If number is even
    else: return bunnyEars(p-1)+3 #If number is add
print(bunnyEars(9)) 