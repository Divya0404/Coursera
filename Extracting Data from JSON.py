
 #Extracting Data from JSON

#In this assignment you will write a Python program somewhat similar to
#http://www.py4e.com/code3/json2.py.
#The program will prompt for a URL,
#read the JSON data from that URL using urllib
#and then parse and extract the comment counts from the JSON data,
#compute the sum of the numbers in the file and enter the sum below

import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = "   Type the URL here   "

html = urllib.request.urlopen(serviceurl).read()

info = json.loads(html)

sum = 0 # A variable to store the result sum

for item in info['comments']:
    sum += int(item['count'])
    
print(sum)


