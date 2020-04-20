
# Extracting Data from XML

#In this assignment you will write a Python program somewhat similar to
#http://www.py4e.com/code3/geoxml.py.
#The program will prompt for a URL,
#read the XML data from that URL using urllib and then
#parse and extract the comment counts from the XML data,
#compute the sum of the numbers in the file


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

serviceurl = " Type the url here"

html = urllib.request.urlopen(serviceurl).read() # To read contents from the url

sum = 0 # To store the result
tree = ET.fromstring(html)

c = tree.findall('.//count') # To find the simple element count from the xml tree

for count in c:
    sum += int(count.text)
print (sum)


