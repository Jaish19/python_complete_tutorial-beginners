import urllib2
response=urllib2.urlopen('www.google.com')
html=response.read()
----------------------------------------------------------------------------

import urllib2

req=urllib2.Request('www.google.com')
resp=urllib2.urlopen(req)
html=resp.read()

-------------------------------------------------------------------------------