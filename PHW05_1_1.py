import urllib.request
import re
import json
from pprint import pprint


while True:                                                       #should throws Exception
    co_code=input("Please enter country code('quit' to quit):")
    if(co_code=='quit'):
        print("Thanks for using!")
        break
    url="https://restcountries.eu/rest/v1/alpha/"+co_code
    page = urllib.request.urlopen(url)
    
    content=page.read()
    content_string = content.decode("utf-8")
    json_data=json.loads(content_string)
    pprint(json_data)
    print("name:",json_data["name"],"capital:",json_data["capital"])