#!/usr/bin/python

import sys,io,requests

# Grab a random quote

r = requests.get('http://quotes.rest/qod.json?category=inspire&maxlength=300') 
data = r.json()
daQuote = data['contents']['quotes'][0]['quote']

print(r)
print(daQuote)