import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.05)

logo = '''
 _    _ _     _ _        ______           _ _ 
| |  | | |   (_) |       |  _  \         (_) |
| |  | | |__  _| |_ ___  | | | |_____   ___| |
| |/\| | '_ \| | __/ _ \ | | | / _ \ \ / / | |
\  /\  / | | | | ||  __/ | |/ /  __/\ V /| | |
 \/  \/|_| |_|_|\__\___| |___/ \___| \_/ |_|_|
                     ______                   
                    |______|                  

'''
animated(logo)
print('''Welcome Sir I am Jarvais ur assistant 
         Made By White_Devil''')
username = "Whitedevil"
password = "1234"
givenUsername = input(" Enter Your username: ")

if givenUsername == username:
    print(" Correct Username ")

givenPassword = input(" Enter Your Password: ")

if givenPassword == password:
    print(" Correct Password ")
else:
    print(" Wrong Username ")
os.system("figlet login in succses")

