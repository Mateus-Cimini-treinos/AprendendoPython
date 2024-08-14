import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim nao esta aceaaivel no momento')
else:
    print('Consegui acessar o site Pudim')