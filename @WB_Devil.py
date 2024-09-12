import webbrowser
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.05)

logo = '''
       ....                        _            .          .. 
   .xH888888Hx.                   u            @88>  x .d88"  
 .H8888888888888:                88Nu.   u.    %8P    5888R   
 888*"""?""*88888X        .u    '88888.o888c    .     '888R   
'f     d8x.   ^%88k    ud8888.   ^8888  8888  .@88u    888R   
'>    <88888X   '?8  :888'8888.   8888  8888 ''888E`   888R   
 `:..:`888888>    8> d888 '88%"   8888  8888   888E    888R   
        `"*88     X  8888.+"      8888  8888   888E    888R   
   .xHHhx.."      !  8888L       .8888b.888P   888E    888R   
  X88888888hx. ..!   '8888c. .+   ^Y8888*""    888&   .888B . 
 !   "*888888888"     "88888%       `Y"        R888"  ^*888%  
        ^"***"`         "YP'                    ""      "%    
'''
animated(logo)
print('             Indias Fast And Seceoure Devil_Browser ')
print('                   »»»Coder By White_Devil««« ')

website = input(" Search_Website: ")
if website == "google":
    print("Google")
    google = input("search:")
    webbrowser.open("https://www.google.co.in/")
elif website == "youtube":
    print("»YouTube«")
    YouTube = input("search:")
    webbrowser.open("https://www.youtube.com/")
elif website == "facebook":
    print("»Facebook«")
    webbrowser.open("https://m.facebook.com/")
elif website == "duckduckgo":
    print("»Duck Duck Go«")
    webbrowser.open("https://duckduckgo.com/")
elif website == "instagram":
    print("»Instagram«")
    webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")

