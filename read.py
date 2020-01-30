import urllib.request
import getpass
print ("Reborn Login")
kullanici_adi=input("Username : ")
sifre=input("Password : ")

if kullanici_adi=="admin" and sifre=='123':
    print("Login Successfully")
elif kullanici_adi=="" or sifre=="":
    print("Please Enter Username or Password")
else:
    print("Login Failed!!")
exit()

try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/4nat/reader/master/.protect.py").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNumber: ' + noti + '\n\n')
except Exception:
    pass


