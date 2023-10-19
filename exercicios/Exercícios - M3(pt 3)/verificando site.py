import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://www.youtube.com/')
except:
    print('\033[31mNão consegui acessar o site YouTube\033[m')
else:
    print('\033[36mConsegui acessar o site YouTube!')
