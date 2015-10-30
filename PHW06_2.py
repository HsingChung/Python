from random import randrange

print("INTEGER DIVISION (enter 'QUIT' to end practice)")
while True:
    try:
        b=randrange(5)
        a=randrange(5)*b
        quot=a/b
        
    except ZeroDivisionError:
        while True:
            b=randrange(5)
            a=randrange(5)*b
            if b!=0:
                quot=a/b                
                break
    try:
       x=input(str(a)+"/"+str(b)+"= ")
       if x=="QUIT":
           print("End practice")
           break
       if int(x)==quot:
           print("CORRECT!")
       else:
           print("INCORRECT!")
    except ValueError:
        print("Please enter INTEGERS only!")