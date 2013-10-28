import urllib
myurl = urllib.urlopen("http://google.com")

print myurl

contents = myurl.readlines()

for line in contents:
	print line + "\n"

headerinfo = myurl.info()

print headerinfo.getheader("date")

print headerinfo.getheader("content-type")


print "----------------"

urllib.urlretrieve("http://google.com",filename = "urlcontent")

