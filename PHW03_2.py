#HW03_P2
#HsingChung Wang
#09/25/2015

def count_frequency(mylist): #define the function
    a={}
    for i in mylist: # for loop
        a[i] = mylist.count(i)
    return a
mylist=["one", "two","eleven",  "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist)) #print the frequency