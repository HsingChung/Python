import os
import pickle

os.chdir("D://courses//5th//Python//HW4")
f=open("DATA.txt","br")
a=pickle.load(f)
print(a)
f.close()