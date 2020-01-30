import urllib.request


try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/4nat/reader/master/.protect.py").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNumber: ' + noti + '\n\n')
except Exception:
    pass

if noti= 0:
    print "x"
else:
    print "y"
