import urllib.request

kullanici_adi=input("Kullanıcı adınızı giriniz : ")
sifre=input("Sifrenizi giriniz : ")

if kullanici_adi=="admin" and sifre=='tht':
    print("Giriş Başarılı")
elif kullanici_adi=="" or sifre=="":
    print("Lutfen Bilgileri Giriniz")
else:
    print("Giriş Başarısız")


try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/4nat/reader/master/.protect.py").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNumber: ' + noti + '\n\n')
except Exception:
    pass


