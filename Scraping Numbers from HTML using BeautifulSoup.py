# Scraping Numbers from HTML using BeautifulSoup.
# In this assignment you will write a Python program similar to
# http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and
# compute the sum of the numbers in the file. 




# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urlopen("Thpe or Copy the url here", context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# To retrieve all span tags
t = soup('span')

sum = 0
for tag in t:
    #To retrieve the contents in the span tag
  sum += int(tag.contents[0])
print(sum)
