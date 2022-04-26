import urllib
import urllib.request

try:
    url = "http://www.pudim.com.br/"
    response = urllib.request.urlopen(url)

except urllib.error.URLError as e:
    print("Ocorreu um erro")
else:
    print("Tudo certo")
finally:
    print(url)
