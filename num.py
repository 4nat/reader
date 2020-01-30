import base64
import urllib.request
a = int(input('sayi: '))
c = urllib.request.urlopen(
"https://raw.githubusercontent.com/4nat/reader/master/a.txt").read()
b=int(base64.b64decode(c))
if a==b:print ("This Number is a Protecting.")
else:print ("Bombing is now started!")


