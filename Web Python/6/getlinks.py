import urllib, htmllib, formatter

website = urllib.urlopen("http://google.com")
data = website.read()
website.close()
Format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
print ptext.anchorlist

for link in ptext.anchorlist:
	print link