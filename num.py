import base64
import urllib.request
a = int(input('Enter Target Number  --> '))
c = urllib.request.urlopen(
"https://raw.githubusercontent.com/4nat/reader/master/a.txt").read()
d = urllib.request.urlopen("https://raw.githubusercontent.com/4nat/reader/master/b.txt").read()
b=int(base64.b64decode(c))
if a==b:print ("This Number is a Protecting.")
elif a==d:print ("This Number is a Protecting.")
else:print ("Bombing is now started!")

