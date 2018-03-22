import urllib2

c=urllib2.urlopen('https://en.wikipedia.org/wiki/Programming_language')
contents=c.read()
print contents 


