import urllib
import urllib.error
import urllib.request

try:
    urllib.request.urlopen('https://www.pudim.com.br')
    print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')
except urllib.error.URLError:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
