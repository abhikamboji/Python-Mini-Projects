import xml.etree.ElementTree as ET
import urllib
import json
from __builtin__ import file
import sqlite3
def week5():
   url = raw_input("Enter location: ")
   print "Retrieving", url
   lib = urllib.urlopen(url)
   file = lib.read()
   et = ET.fromstring(file)
   count = et.findall(".//count")
   sum = 0
   for value in count:
       sum = sum + int(value.text)
   print "Retrieved", len(file), "characters"
   print "Count:", len(count)
   print sum
def week6():
    input = raw_input("Enter location")
    print "Retrieving", input
    url = urllib.urlopen(input)
    file = url.read()
    js = json.loads(file)
    sum = 0
    for comment in js["comments"]:
        sum = sum + int(comment["count"])
    print sum
def week6_2():
    sourceUrl = "http://python-data.dr-chuck.net/geojson?"
    while True:
        loc = raw_input("Location")
        if len(loc)< 1:
            break
        url = sourceUrl + urllib.urlencode({"sensor":"false", "address": loc})
        print url
        http = urllib.urlopen(url)
        file = http.read()
        try: 
            js = json.loads(str(file))
        except: 
            js = None
        if loc not in js or js[loc] != 'OK':
            print '==== Failure To Retrieve ===='
            print file
            continue
        print json.dumps(js, indent=4)
        print js["results"][0]["place_id"]
week6_2()
def week6_2_5():
    
# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    serviceurl = 'http://python-data.dr-chuck.net/geojson?'

    while True:
        address = raw_input('Enter location: ')
        if len(address) < 1 : break

        url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
        print 'Retrieving', url
        uh = urllib.urlopen(url)
        data = uh.read()
        print 'Retrieved',len(data),'characters'

        try: js = json.loads(str(data))
        except: js = None
        if 'status' not in js or js['status'] != 'OK':
            print '==== Failure To Retrieve ===='
            print data
            continue
    
        print json.dumps(js, indent=4)
    
        lat = js["results"][0]["place_id"]
        print lat
def 