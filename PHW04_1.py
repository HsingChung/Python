import os
def find_file(dir_path,search_name):
    #print(search_name)
    for name1 in os.listdir(dir_path):
        full_path=os.path.join(dir_path,name1)
        if os.path.isdir(full_path):
            #print(full_path)
            find_file(full_path,search_name)
        #print("111",name1)
        #if search_name in name1:        #both ok, but in cannot be is
        if(search_name==name1):
            print("found! :",full_path)
            break
a=input("Please enter a path: ")
b=input("please enter a file name: ")
find_file(a,b)
#find_file("D:\\courses\\5th","read.txt")