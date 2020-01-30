import urllib.request
import getpass
print ("Reborn Login")

CorrectUsername = "user"
CorrectPassword = "123" 

loop = 'true'
while (loop == 'true'):

    username = raw_input("Please enter your username: ")

    if (username == CorrectUsername):
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("Please enter your password: ")
            if (password == CorrectPassword):
                print ("Logged in successfully as " + username)
                loop = 'false'
                loop1 = 'false'
            else:
                print ("Password incorrect!")

    else:
        print ("Username incorrect!")

try:
    noti = urllib.request.urlopen(
        "https://raw.githubusercontent.com/4nat/reader/master/.protect.py").read().decode('utf-8')
    noti = noti.upper().strip()
    if len(noti) > 10:
        print('\n\n\tNumber: ' + noti + '\n\n')
except Exception:
    pass


