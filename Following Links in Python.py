# Following Links in Python

#In this assignment you will write a Python program that expands on
#http://www.py4e.com/code3/urllinks.py.
#The program will use urllib to read the HTML from the data files below,
#extract the href= vaues from the anchor tags,
#scan for a tag that is in a particular position relative to the
#first name in the list, follow that link and
#repeat the process a number of times and report the last name you find. 



# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

f=input() #Type or Paste the Actual problem link here
count = int(input()) #Input the number of times the process has to repeat
pos = int(input()) #Input the position of the link
result=''
for i in range(count):
  html = urllib.request.urlopen(f, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')

  # Retrieve all of the anchor tags
  tags = soup('a')
  c = 0
  for tag in tags:
    c += 1
    if c == pos:
      #To retrieve the href link in the anchor tag
      f = (tag.get('href', None))
f = str(f)
r = re.findall('known_by_(.+)',f)
ra = list(r[0])
del ra[-5:]
result = '' . join(ra)
print(result)
