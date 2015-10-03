import os
os.chdir("D:\\courses\\5th\\python\\HW4")
file_name=input("Please enter a file name: ")
out = open(file_name,"r")
a = True
while a:
    line=out.readline()
    if not line:
        print("no password")
        break
    if "password=" in line:
        print("password")
        a=False