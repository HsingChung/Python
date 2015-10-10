import urllib.request
import re

page = urllib.request.urlopen("https://restcountries.eu/rest/v1/alpha/co")
content=page.read()
content_string = content.decode("utf-8")
a_dic = eval(content_string)
#print(a_dic)
while True:
    co_code=input("Please enter country code('quit' to quit):")

    if(co_code=='quit'):
        print("Thanks for using!")
        break
    regexp = re.compile(co_code)
    if(regexp.search(co_code)):
        print("name:",a_dic["name"],"capital:",a_dic["capital"])
   # else:
    #    print("not found")
    if(regexp.match(co_code)==True):
        print(a_dic[co_code])
    else:
        print("not found")