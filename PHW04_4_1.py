import os
import pickle

os.chdir("D://courses//5th//Python//HW4")
f=open("DATA.txt","bw")
dic={}
dic["name"]=input("name: ")
dic["age"]=input("age: ")
dic["country"]=input("country: ")
pickle.dump(dic,f)
f.close()