import urllib.request
import getpass
print ("Reborn Login")
kullanici_adi=input("Username : ")
sifre=input("Password : ")

if kullanici_adi=="admin" and sifre=='123':
    print("Welcome Sir!")
pnumber=input("Protect Your Number : ")
exit()
else:
    print("Login Failed!!")
exit()


